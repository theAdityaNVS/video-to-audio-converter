# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Video To Audio Converter (V 1.0) (Windows).py'],
             pathex=['C:\\Users\\Aditya Nadamuni\\Documents\\Python Projects\\Video To Audio Converter'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Video To Audio Converter (V 1.0) (Windows)',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Video To Audio Converter (V 1.0) (Windows)')
