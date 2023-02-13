#
# spec file for package openssl_tpm2_engine
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2017 James.Bottomley@HansenPartnership.com
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           openssl_tpm2_engine
Version:        2.4.2
Release:        2
Summary:        OpenSSL TPM 2.0 interface engine plugin
License:        LGPL-2.1-only
Group:          Productivity/Security
URL:            https://git.kernel.org/pub/scm/linux/kernel/git/jejb/openssl_tpm2_engine.git/
Source0:        https://git.kernel.org/pub/scm/linux/kernel/git/jejb/openssl_tpm2_engine.git/snapshot/%{name}-%{version}.tar.gz
Patch0:         Add-openssl-3-support.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  help2man
BuildRequires:  tss2
BuildRequires:  tss2-devel
BuildRequires:  libtool
BuildRequires:  openssl-devel
Requires: openssl-libs

%description
This package contains a plugin a for OpenSSL which connects it with the
Trusted Platform Module version 2.0 found on newer machines and a
create_tpm2_key helper binary to create and extract a TPM key.

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fiv
%configure --libdir=/%{_lib}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%define EXTRA_FILES ExtraFiles.list
CWD=`pwd`
cd %{buildroot}
touch $CWD/%{EXTRA_FILES}
find * -name \*.so -printf "/%p\n" > $CWD/%{EXTRA_FILES}

%files -f %{EXTRA_FILES}
%license LICENSE
%doc README openssl.cnf.sample
%{_bindir}/*
%{_mandir}/man1/*

%changelog

* Tue Feb  7 11:48:56 CET 2023 - Roberto Sassu <roberto.sassu@huawei.com>
- Add Add-openssl-3-support.patch to fix a build issue

* Fri Jul  3 09:35:56 UTC 2020 - Pedro Monreal Gonzalez <pmonrealgonzalez@suse.com>
- Update tarball due to download_files error

* Thu Jul  2 15:03:09 UTC 2020 - James.Bottomley@HansenPartnership.com
- Update to version 2.4.2
  * Add every TPM supported curve (as defined by the TCG)
  * Fix a bug with explicitly parametrised curve handling (needed for BN)
  * Update the tests to be able to use swtpm
  * Allow loading public key without password

* Thu Mar 26 04:31:36 UTC 2020 - James.Bottomley@HansenPartnership.com
- Update to version 2.4.1
  * fixes for older OpenSSL and gcc
  * variable tpm_server location for testing

* Fri Mar 6 00:47:24 UTC 2020 - James.Bottomley@HansenPartnership.com
- Update to version 2.4.0
  * data seal/unseal handling
  * PKCS12 wrapping support

* Fri Jan 10 16:52:22 UTC 2020 - James.Bottomley@HansenPartnership.com
- Update to version 2.3.1
  * bug fixes
  * add handling for DER keys

* Sun Feb 24 17:10:22 UTC 2019 - James.Bottomley@HansenPartnership.com
- Update to version 2.3.0
  * add the ability to produce restricted (storage) keys with defined
    symmetric seeds
  * new load_tpm2_key command to load a key file at a NV index
- Version 2.2.0
  * Add support for non-PKCS1 padding
  * Fixups for engines and cross builds

* Wed Nov 14 14:43:17 PST 2018 - James.Bottomley@HansenPartnership.com
- Update to version 2.1.0:
  * Add importable keys feature

* Mon Nov 12 21:04:09 PST 2018 - James.Bottomley@HansenPartnership.com
- Update to version 2.0.1:
  * Fix name algorithm selection
  * Make policy correct for non sha256 name algorithms
  * add security to TPM decryption operations

* Mon Nov  5 07:37:09 PST 2018 - James.Bottomley@HansenPartnership.com
- Update to version 2.0.0:
  * Licence changed from GPL to LGPL (fixes openssl compatibility)
  * Key format changed for interoperability
  * OIDs updated with input from the TCG (new format only)

* Sat Aug 10 08:05:00 PDT 2018 - James.Bottomley@HansenPartnership.com
- Update to version 1.2.1:
  * Policy file support (fixed)
