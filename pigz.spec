#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
#
Name     : pigz
Version  : 2.7
Release  : 49
URL      : https://zlib.net/pigz/pigz-2.7.tar.gz
Source0  : https://zlib.net/pigz/pigz-2.7.tar.gz
Summary  : pigz is a parallel implementation of gzip which utilizes multiple cores
Group    : Development/Tools
License  : Apache-2.0 Zlib
Requires: pigz-bin = %{version}-%{release}
Requires: pigz-license = %{version}-%{release}
Requires: pigz-man = %{version}-%{release}
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Add-make-install-for-pigz.patch
Patch2: rsync.patch
Patch3: link.patch
Patch4: error.patch
Patch5: build.patch

%description
pigz, which stands for parallel implementation of gzip, is a fully functional replacement for gzip that exploits multiple processors and multiple cores to the hilt when compressing data. pigz was written by Mark Adler, and uses the zlib and pthread libraries.

%package bin
Summary: bin components for the pigz package.
Group: Binaries
Requires: pigz-license = %{version}-%{release}

%description bin
bin components for the pigz package.


%package license
Summary: license components for the pigz package.
Group: Default

%description license
license components for the pigz package.


%package man
Summary: man components for the pigz package.
Group: Default

%description man
man components for the pigz package.


%prep
%setup -q -n pigz-2.7
cd %{_builddir}/pigz-2.7
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
pushd ..
cp -a pigz-2.7 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1683127691
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
make  %{?_smp_mflags}

pushd ../buildavx2
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1683127691
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pigz
cp %{_builddir}/pigz-%{version}/zopfli/COPYING %{buildroot}/usr/share/package-licenses/pigz/6d182cfd7e2a6c633140f7cdb0c4a46fc4a23589 || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/gzip
/V3/usr/bin/pigz
/usr/bin/gzip
/usr/bin/pigz

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pigz/6d182cfd7e2a6c633140f7cdb0c4a46fc4a23589

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/pigz.1
