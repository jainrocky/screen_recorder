# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['PyRecorder.py'],
             pathex=['C:\\Users\\Rocky Jain\\Desktop\\PyRecorder'],
             binaries=[],
             datas=[('C:\\Python3.7.4\\Lib\\site-packages\\cv2\\opencv_ffmpeg410_64.dll', '.')],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='PyRecorder',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
