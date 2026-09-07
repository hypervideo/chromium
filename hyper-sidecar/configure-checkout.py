from pathlib import Path
Path('.gclient').write_text('''solutions = [{
  "name": "src",
  "url": "https://github.com/hypervideo/chromium.git",
  "managed": False,
  "custom_deps": {},
  "custom_vars": {
    "checkout_configuration": "small",
    "checkout_pgo_profiles": True,
    "checkout_js_coverage_modules": False,
  },
}]
''')
