# Hyper sidecar Chromium experiment

This branch starts from Chromium 147.0.7727.15, commit
`6b5a1b80ccc1e8a4967901d8e58fc2e162cdf050`, to compare against the browser
currently used by Hyper's room sidecar.

It builds the headless shell with release PGO/ThinLTO and size optimization.
WebRTC, audio/video codecs, Web Audio, MediaRecorder, rendering, WebGL and
SwiftShader remain enabled. PDF, printing, extensions, desktop integrations,
Vulkan validation layers and the bundled DevTools UI are omitted. Puppeteer's
DevTools protocol remains available; the unbundled `/json/protocol` schema
endpoint returns 404 instead of aborting.

Run the manually dispatched `Hyper headless Chromium` workflow to produce an
experimental Linux x64 artifact. A successful compile is not meeting acceptance:
the artifact must pass Hyper's browser lifecycle, live-call audio, video decode,
recording/replay and matched resource/startup checks before adoption. No runtime
performance improvement is claimed by this branch alone.

The only compiler patch limits ThinLTO to four link workers for the build
machine. The other patches make upstream's DevTools frontend switch configurable
and make headless packaging respect it. Keep these patches small when updating
the pinned Chromium revision; this experiment is not an automatic security
update mechanism.
