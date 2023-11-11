from setuptools import setup

minha_lista = [1,2,3,4,5]

setup(
    name='teste'
    , version='0.0.1'
    , description="Python module teste"
    , author='João Paulo de Brito e Cautter'
    , author_email='jcautter@gmail.com'
#     , url='https://github.com/nvbn/import_from_github_com'
    , license='MIT'
#     , packages=find_packages(
#         exclude=[
#             'ez_setup'
#             , 'examples'
#             , 'tests'
#             , 'release'
#         ]
#     )
    , include_package_data=True
    , zip_safe=False
)
