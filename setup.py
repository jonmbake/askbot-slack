from setuptools import setup

setup(
    name="askbot-slack",
    version="0.2.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    packages=['askbot_slack'],
    install_requires=['askbot', 'requests'],
    author="Jon Bake",
    author_email="jonmbake@gmail.com",
    description="Simple Slack integration for Askbot.",
    long_description="When questions are created, edited or responded to in Askbot a message is sent to a specified channel in Slack.",
    license="MIT",
    keywords="askbot slack integration",
    url="https://github.com/jonmbake/askbot-slack",
)
