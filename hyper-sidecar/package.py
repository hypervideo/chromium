import hashlib,json,os,pathlib,shutil,subprocess
root=pathlib.Path.cwd()
out=root/'out/HyperHeadless'
package=root/'hyper-headless-linux-x64'
package.mkdir(exist_ok=True)
for name in ['headless_shell','chrome_crashpad_handler','libEGL.so','libGLESv2.so','libvk_swiftshader.so','vk_swiftshader_icd.json','libvulkan.so.1']:
 path=out/name
 if not path.is_file():raise RuntimeError('Missing runtime file: '+name)
 shutil.copy2(path,package/name)
shutil.copy2(root/'LICENSE',package/'LICENSE')
shutil.copy2(root/'hyper-sidecar/args.gn',package/'args.gn')
subprocess.run(['python3','tools/licenses/licenses.py','credits','--target-os=linux','--gn-out-dir='+str(out),'--gn-target=//headless:headless_shell',str(package/'CREDITS.html')],check=True,env={**os.environ,'LICENSES_GN_PATH':str(root/'hyper-sidecar/gn-headless.py')})
version=subprocess.check_output([str(package/'headless_shell'),'--version'],text=True).strip()
manifest={'version':version,'sourceRevision':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'files':{p.name:{'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(package.iterdir()) if p.is_file()}}
(package/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
subprocess.run(['tar','--zstd','-cf',str(root/'hyper-headless-linux-x64.tar.zst'),'-C',str(root),package.name],check=True)
print(json.dumps(manifest,indent=2))
