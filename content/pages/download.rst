Download
########

:url: download/
:save_as: download/index.html
:date: 2021-02-20 12:00

.. contents:: Links

We provide pre-built packages for `Windows <#windows>`__, `macOS <#macos>`__, and some `Linux <#linux>`__ distributions.

You can also download the `source code <#source>`__ and build it yourself, or `look for a package <https://repology.org/metapackage/taisei/versions>`__ in your distribution's repositories.

If you're looking for PGP signatures, SHA256 sums, or older releases, visit the `releases page on GitHub <https://github.com/taisei-project/taisei/releases>`__.

If you find any mistakes, please contact us.

----

Windows
"""""""

Stable
''''''

* `w64s`_
* `w32s`_
* `w64z`_
* `w32z`_

If in doubt, try the 64-bit installer first.

.. _w64s: windows-x64-setup!
.. _w32s: windows-x86-setup!
.. _w64z: windows-x64-zip!
.. _w32z: windows-x86-zip!

----

Linux
"""""

Arch Linux
''''''''''

There are unofficial `taisei <https://aur.archlinux.org/packages/taisei/>`__
and `taisei-git <https://aur.archlinux.org/packages/taisei-git/>`__
PKGBUILDs available on `AUR <http://aur.archlinux.org/>`__.

Open Build Service
''''''''''''''''''

{% for title, stable, suffix in [("Stable", "yes", ":stable"), ("Development Snapshots", "no", "")] %}

`{{ title }} <https://build.opensuse.org/project/show/home:lachs0r:taisei{{ suffix }}>`__

{% for distro in ["Fedora 29"] %}

.. collapsible::
    :name: {{ distro }}
    :stable: {{ stable }}

    dnf config-manager --add-repo https://download.opensuse.org/repositories/home:/lachs0r:/taisei{% if stable %}:/stable{% endif %}/{{ distro|replace(" ", "_") }}/home:lachs0r:taisei{% if stable %}:stable{% endif %}.repo
    dnf install taisei


{% endfor %}

{% for distro in [
    "openSUSE Tumbleweed",
    "openSUSE Leap 15.0",
    "openSUSE Leap 15.1",
] %}

.. collapsible::
   :name: {{ distro }}
   :stable: {{ stable }}

    zypper ar -fr https://download.opensuse.org/repositories/home:/lachs0r:/taisei{% if stable %}:/stable{% endif %}/{{ distro|replace(" ", "_") }}/home:lachs0r:taisei{% if stable %}:stable{% endif %}.repo
    zypper in taisei

{% endfor %}
{% endfor %}

Flatpack
''''''''

An `unofficial package <https://www.flathub.org/apps/details/org.taisei_project.Taisei>`__ is available on Flathub.

Static Build
''''''''''''

* `linux`_

This is a relocatable, (mostly) statically-linked build that should work on most glibc-based Linux distributions without installation. If possible, we recommend using your distribution's package or our OBS repos instead of this.

.. _linux: linux!

----

macOS
"""""

* `macos`_

.. _macos: macos!

----

Switch (Homebrew)
"""""""""""""""""

* `switch`_

This is a semi-official port for the Switch console. You can also `get it on the Homebrew Appstore <https://www.switchbru.com/appstore/#/app/Taisei>`__.

**Use at your own risk.** Contact `@p-sam <https://twitter.com/p__sam>`__ for support.

.. _switch: switch!

----

Source Code
"""""""""""

.. role:: bash(code)
   :language: bash

Building Taisei is easy (unless you are on Windows).

Download the source code and follow the instructions in :bash:`README.md`.

Feel free to contact us if you have problems.

Although Taisei supports only Linux, macOS, and Windows officially, it's also known to work on BSD systems and Haiku.

Generally, it should build and run on any POSIX-compliant OS, given that `all the dependencies <https://github.com/taisei-project/taisei/#dependencies>`__ also work there.

Stable
''''''

* `source`_

.. _source: source!

Unstable
''''''''

.. class:: codeblock

    git clone --recurse-submodules -j8 https://github.com/taisei-project/taisei
