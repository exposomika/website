# Asset provenance

- `assets/logo.png`: existing exposomika logo provided in the workspace, preserved unchanged.
- `assets/favicon.svg`: simple vector asterisk, created for the site's indigo and amber identity.
- `assets/exposure-field.png`: original decorative hero artwork, generated once with the built-in **imagegen** tool on 8 October 2026. This is abstract brand imagery, not measured data, microscopy, or a scientific model.

## Exact hero prompt

```text
Use case: stylized-concept
Asset type: Original bitmap website hero artwork for exposomika, a science startup measuring environmental exposures to understand their impact on individual health.
Primary request: Highly refined editorial scientific art: a softly luminous translucent sphere, a field of delicate particulate filaments, atmospheric environmental particles folding into a subtle organic central core. A scientific instrument's mysterious field of view.
Scene/backdrop: Deep midnight-indigo background with subtle tones from #171334 to #29215d.
Style/medium: Sophisticated abstract scientific artwork with tactile fine grain, ethereal volumetric light, and delicately detailed particles.
Composition/framinging: Wide landscape 3:2, approximately 1536x1024. Position the luminous sphere and main form right-center; preserve generous dark negative space on the left. Complete artwork with no frame.
Lighting/mood: Restrained, atmospheric and luminous. Smoky lilac-white particles with a restrained amber (#ee9900) luminous current threading through the form.
Constraints: No literal brain, human, DNA helix, medical cross, dashboards, text, labels, UI, logos, or watermarks. Create exactly one image.
```

The saved bitmap is an input to the reproducible Quarto render; rendering never calls an image-generation service.
