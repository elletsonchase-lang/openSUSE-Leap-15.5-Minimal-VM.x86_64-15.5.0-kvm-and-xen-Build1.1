#
# spec file for package kiwi-templates-Minimal
#
# Copyright (c) 2022 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define dest %_datadir/kiwi/image/openSUSE-Leap-15-Minimal

%if "@BUILD_FLAVOR@" != ""
ExclusiveArch: do_not_build
%endif

Name:           kiwi-templates-Minimal
Version:        15.5
Release:        0
BuildArch:      noarch
License:        MIT
Summary:        KIWI - openSUSE Leap 15 Minimal image templates
Url:            https://www.suse.com/
Group:          System/Management
Source01:       config.sh
Source02:       Minimal.kiwi
Source03:       editbootinstall_rpi.sh
Source99:       LICENSE
Provides:       kiwi-templates-JeOS = %{version}
Obsoletes:      kiwi-templates-JeOS < %{version}
Requires:       python3-kiwi
Supplements:    kiwi-templates

%description
This package contains system image templates to easily build
an openSUSE Leap 15 based operating system image with
kiwi.

%prep
%setup -cT
cp "%SOURCE99" .

%build

%install
dst="%buildroot%dest"
mkdir -p $dst
for i in %{SOURCE1} %{SOURCE2} %{SOURCE3}; do
	install -m 644 $i "$dst"
done

%files
%license LICENSE
%dest
%_datadir/kiwi/

%changelog
