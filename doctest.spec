%global debug_package %{nil}

Name: doctest
Version: 2.4.9
Release: %mkrel 1
Summary: Feature-rich header-only C++ testing framework
License: MIT
URL: https://github.com/doctest/doctest
Source0: https://github.com/doctest/doctest/archive/v%{version}/%{name}-%{version}.tar.gz
Group: Development/C++

BuildRequires: gcc-c++
BuildRequires: cmake3
BuildRequires: git-core

%description
A fast (both in compile times and runtime) C++ testing framework, with the
ability to write tests directly along production source (or in their own
source, if you prefer).

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: libstdc++-devel%{?_isa}

%description devel
%{summary}.

%prep
%autosetup -p1

%build
%cmake \
  -DDOCTEST_WITH_MAIN_IN_STATIC_LIB:BOOL=OFF \
  -DDOCTEST_WITH_TESTS:BOOL=ON
%cmake_build

%check
%ctest

%install
%cmake_install

%files devel
%doc README.md CHANGELOG.md CONTRIBUTING.md
%license LICENSE.txt
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
