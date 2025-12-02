from setuptools import setup

if __name__ == "__main__":
    from setuptools import setup

    with open('requirements.txt') as f:
        required = f.read().splitlines()

    # All metadata/config is in setup.cfg
    setup(install_requires=required)
