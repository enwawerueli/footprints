# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=[
                '/home/enwawerueli/workspace/footprints',
                '/usr/lib64/python2.7/site-packages'],
             binaries=[],
             datas=[
                ('README.md', '.'),
                ('app/db/storage.sqlite3', 'app/db'),
                ('app/ui/res', 'app/ui/res')
            ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='footprints',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='footprints')
