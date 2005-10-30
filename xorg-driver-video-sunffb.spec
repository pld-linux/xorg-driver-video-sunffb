Summary:	X.org video driver for Sun Creator, Creator 3D and Elite 3D video cards
Summary(pl):	Sterownik obrazu X.org dla kart graficznych Sun Creator, Creator 3D i Elite 3D
Name:		xorg-driver-video-sunffb
Version:	1.0.0.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/driver/xf86-video-sunffb-%{version}.tar.bz2
# Source0-md5:	f5179f85fc6ac46e5410bc1e0851b38f
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRequires:	xorg-xserver-server-devel
ExclusiveArch:	sparc sparcv9 sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Sun Creator, Creator 3D and Elite 3D video
cards.

%description -l pl
Sterownik obrazu X.org dla kart graficznych Sun Creator, Creator 3D i
Elite 3D.

%prep
%setup -q -n xf86-video-sunffb-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	drivermandir=%{_mandir}/man4

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/sunffb_drv.so
%{_mandir}/man4/sunffb.4x*
