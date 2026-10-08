"use strict";

// Progressive enhancement: all exposure descriptions remain available without JS.
const tablist = document.querySelector(".exposure-tabs");
if (tablist) {
  const tabs = [...tablist.querySelectorAll("button")];
  const panels = tabs.map((tab) => document.getElementById(tab.dataset.panel));
  tablist.setAttribute("role", "tablist");

  function activate(index, focus = false) {
    tabs.forEach((tab, current) => {
      const selected = current === index;
      tab.setAttribute("aria-selected", String(selected));
      tab.tabIndex = selected ? 0 : -1;
      panels[current].hidden = !selected;
    });
    if (focus) tabs[index].focus();
  }

  tabs.forEach((tab, index) => {
    tab.setAttribute("role", "tab");
    tab.setAttribute("aria-controls", panels[index].id);
    panels[index].setAttribute("role", "tabpanel");
    panels[index].setAttribute("aria-labelledby", tab.id);
    panels[index].tabIndex = 0;
    tab.addEventListener("click", () => activate(index));
    tab.addEventListener("keydown", (event) => {
      let next;
      if (event.key === "ArrowRight") next = (index + 1) % tabs.length;
      if (event.key === "ArrowLeft") next = (index - 1 + tabs.length) % tabs.length;
      if (event.key === "Home") next = 0;
      if (event.key === "End") next = tabs.length - 1;
      if (next !== undefined) {
        event.preventDefault();
        activate(next, true);
      }
    });
  });
  activate(0);
  tablist.classList.add("enhanced");
}
