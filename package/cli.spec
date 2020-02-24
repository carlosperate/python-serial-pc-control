# -*- mode: python ; coding: utf-8 -*-

DEBUG = False

block_cipher = None


a = Analysis(['../serial_pc_control/cli.py'],
             pathex=['../'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=DEBUG)

pyz = PYZ(a.pure,
          a.zipped_data,
          cipher=block_cipher)

if not DEBUG:
    exe = EXE(pyz,
              a.scripts,
              a.binaries,
              a.zipfiles,
              a.datas,
              [],
              name='SerialPcControl',
              debug=False,
              bootloader_ignore_signals=False,
              strip=False,
              upx=True,
              upx_exclude=[],
              runtime_tmpdir=None,
              console=True)
else:
    exe = EXE(pyz,
              a.scripts,
              [('v', None, 'OPTION')],
              exclude_binaries=True,
              name='SerialPcControl',
              debug=True,
              bootloader_ignore_signals=False,
              strip=False,
              upx=True,
              console=True)
    coll = COLLECT(exe,
                   a.binaries,
                   a.zipfiles,
                   a.datas,
                   strip=False,
                   upx=True,
                   upx_exclude=[],
                   name='SerialPcControl')
