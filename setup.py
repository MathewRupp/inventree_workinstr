import setuptools

setuptools.setup(
    name="inventree-workinstr-plugin",
    version="0.1.0",
    author="Mathew Rupp",
    description="Show a Work Instructions link panel on Part detail pages in InvenTree",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "inventree_plugins": [
            "WorkInstrPlugin = inventree_workinstr.workinstr:WorkInstrPlugin"
        ]
    },
)
