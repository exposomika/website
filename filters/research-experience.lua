-- Calculate experience from the supplied start years and an explicit reference
-- year. Keeping the year in index.qmd makes historical renders reproducible.
-- This uses Pandoc's bundled Lua runtime; no additional dependencies are needed.
function Pandoc(doc)
  local function number(key)
    local value = tonumber(pandoc.utils.stringify(doc.meta[key]))
    assert(value and value % 1 == 0, "Expected an integer metadata value: " .. key)
    return value
  end
  local as_of = number("research-as-of")
  local manuel = as_of - number("research-start-manuel")
  local salma = as_of - number("research-start-salma")
  assert(manuel >= 0 and salma >= 0, "Research start years must precede the reference year")
  local values = { ["as-of"] = as_of, manuel = manuel, salma = salma }
  return doc:walk({
    RawBlock = function(block)
      if block.format == "html" then
        block.text = block.text:gsub("@@research:([%w-]+)@@", function(key)
          assert(values[key], "Unknown research experience key: " .. key)
          return tostring(values[key])
        end)
        return block
      end
    end
  })
end
