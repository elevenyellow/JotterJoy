# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src/jotterjoy/app/main.py'],
    pathex=[],
    binaries=[],
    datas=[('src/jotterjoy/prompts/fix_text.txt', 'src/jotterjoy/prompts'), ('src/jotterjoy/prompts/generate_title.txt', 'src/jotterjoy/prompts'), ('src/jotterjoy/prompts/tagging.txt', 'src/jotterjoy/prompts')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='jotterjoy',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
