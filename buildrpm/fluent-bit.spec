

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

%global app_name                fluent-bit
%global app_version             4.1.2
%global oracle_release_version  1
%global _buildhost              build-ol%{?oraclelinux}-%{?_arch}.oracle.com

Name:           %{app_name}
Version:        %{app_version}
Release:        %{oracle_release_version}%{?dist}
Summary:        Telemetry agent for logs, metrics, and traces.
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/fluent/fluent-bit.git
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  git
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  libyaml-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  libicu
BuildRequires:  libicu-devel
BuildRequires:  libpq
BuildRequires:  libpq-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  systemd-devel
BuildRequires:  zlib-devel
BuildRequires:  postgresql
BuildRequires:  postgresql-server
BuildRequires:  cpio

%description
Telemetry agent for logs, metrics, and traces.

%prep
%setup -q -n %{name}-%{version}

%build
cd build
cmake -DFLB_RELEASE=On \
    -DFLB_JEMALLOC=On \
    -DFLB_TLS=On \
    -DFLB_SHARED_LIB=Off \
    -DFLB_EXAMPLES=Off \
    -DFLB_HTTP_SERVER=On \
    -DFLB_IN_EXEC=Off \
    -DFLB_IN_SYSTEMD=On \
    -DFLB_OUT_KAFKA=On \
    -DFLB_OUT_PGSQL=On \
    -DFLB_JEMALLOC_OPTIONS="--with-lg-vaddr=48" \
    -DFLB_LOG_NO_CONTROL_CHARS=On \
    ..
make -j "$(getconf _NPROCESSORS_ONLN)"

%install
install -m 755 -d %{buildroot}/%{app_name}/bin
install -m 755 build/bin/%{app_name} %{buildroot}/%{app_name}/bin/${app_name}

%files
%license LICENSE THIRD_PARTY_LICENSES.txt olm/SECURITY.md
/%{app_name}/

%changelog
* Wed Dec 10 2025 Oracle Cloud Native Environment Authors <noreply@oracle.com> - 4.1.2-1
- Added Oracle specific build files for fluent-bit.
