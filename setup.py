import os
from setuptools import setup, find_packages

__here__ = os.path.dirname(os.path.abspath(__file__))

package_info = dict.fromkeys(["RELEASE", "COMMIT", "VERSION", "NAME"])

for name in package_info:
    with open(os.path.join(__here__, "insights", name)) as f:
        package_info[name] = f.read().strip()

entry_points = {
    'console_scripts': [
        'insights-run = insights.core:main',
        'gen_api = insights.tools.generate_api_config:main',
        'insights-perf = insights.tools.perf:main',
        'client = insights.client:run',
        'mangle = insights.util.mangle:main'
    ]
}

runtime = set([
    'pyyaml>=3.10,<=3.12',
    'six',
])

try:
    import importlib # noqa
except ImportError:
    runtime.add("importlib")

try:
    import argparse # noqa
except ImportError:
    runtime.add("argparse")

client = set([
    'requests',
    'pyOpenSSL',
])

develop = set([
    'flake8==3.3.0',
    'coverage==4.3.4',
    'pytest==3.0.6',
    'pytest-cov==2.4.0',
    'Sphinx',
    'nbsphinx==0.3.1',
    'sphinx_rtd_theme',
    'futures==3.0.5',
    'requests==2.13.0',
    'wheel',
    'ipython<6',
])

if __name__ == "__main__":
    # allows for runtime modification of rpm name
    name = os.environ.get("INSIGHTS_CORE_NAME", package_info["NAME"])

    setup(
        name=name,
        version=package_info["VERSION"],
        description="Insights core execution framework and rule API",
        long_description=open("README.rst").read(),
        url="https://github.com/redhatinsights/insights-core",
        author="Red Hat, Inc.",
        author_email="insights@redhat.com",
        packages=find_packages(),
        install_requires=list(runtime),
        package_data={'': ['LICENSE']},
        license='Apache 2.0',
        extras_require={
            'develop': list(runtime | develop | client),
            'client': list(runtime | client),
            'optional': ['python-cjson', 'python-logstash', 'python-statsd', 'watchdog'],
        },
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Natural Language :: English',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7'
        ],
        entry_points=entry_points,
        include_package_data=True
    )
