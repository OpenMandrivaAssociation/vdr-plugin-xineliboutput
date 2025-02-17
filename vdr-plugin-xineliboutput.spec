
%define plugin	xineliboutput
%define name	vdr-plugin-%plugin
# manually created tarball from CVS tag
%define version	1.0.5
%define snapshot 0
%define prever	0
%define rel	4
# Please update xine-xvdr as well.
# It uses the same tarball but builds xine1.2-xvdr subpackage
# equivalent for stable xine.

%if %snapshot
%if %prever
%define release	%mkrel 0.%prever.%snapshot.%rel
%else
%define release %mkrel 0.%snapshot.%rel
%endif
%else
%if %prever
%define release %mkrel 0.%prever.%rel
%else
%define release %mkrel %rel
%endif
%endif

%define xineplugindir	%(xine-config --plugindir 2>/dev/null || echo 0)
# Does not always match rpm version, reports 1.1.9 on 1.1.9.1, so use rpmver directly instead.
#define xineversion	%(xine-config --version 2>/dev/null || echo 0)
%define xineversion	%(rpm -qf --qf '%%{version}' %{_bindir}/xine-config 2>/dev/null || echo 0)
%define xineapi		%(A=%xineplugindir; echo ${A##*/})

Summary:	VDR plugin: X11/xine-lib output plugin
Name:		%name
Version:	%version
Release:	%release
Group:		Video
License:	GPLv2+
URL:		https://sourceforge.net/projects/xineliboutput/
%if %snapshot
Source:		vdr-%plugin-%snapshot.tar.bz2
%else
%if %prever
Source:		http://prdownloads.sourceforge.net/xineliboutput/vdr-%plugin-%{version}%{prever}.tar.bz2
%else
Source:		http://prdownloads.sourceforge.net/xineliboutput/vdr-%plugin-%version.tar.bz2
%endif
%endif
# fix build with libextractor 0.6+, from upstream:
Patch0:		xineliboutput-extractor-metainfo-menu1.patch
Patch1:		xineliboutput-extractor-metainfo-menu2.patch
Patch2:		xineliboutput-extractor-playlist.patch
Patch3:		xineliboutput-extractor-playlist2.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
BuildRequires:	libx11-devel
BuildRequires:	libxv-devel
BuildRequires:	xine1.2-devel
BuildRequires:	jpeg-devel
BuildRequires:	libextractor-devel
BuildRequires:	libxrender-devel
BuildRequires:	libxinerama-devel
BuildRequires:	dbus-glib-devel
Requires:	vdr-abi = %vdr_abi

%description
Framebuffer and/or X11 front-end for VDR. Displays OSD and video in
a raw X/Xv/XvMC window, Linux framebuffer/DirectFB or xine.

Support for local and standalone ("remote") frontends. The plugin is
able to use local pipe, RTP/UDP multicast, UDP unicast and TCP to
transfer the data to the standalone clients.

Built-in image and media player supports playback of most known
media files and network radio/video streams directly from VDR.

Frontend packages:
- xine-xvdr: Xine frontend
- xine1.2-xvdr: Xine1.2 frontend
- xineliboutput-sxfe: Standalone X11 frontend
- xineliboutput-fbfe: Standalone FB frontend
- xineliboutput-local-sxfe: Local X11 frontend
- xineliboutput-local-fbfe: Local FB frontend

%package -n xine1.2-xvdr
Group:		Video
Summary:	Xine frontend for the xineliboutput VDR plugin
Requires:	%{_lib}xine2-plugin-api >= %xineapi
Provides:	vdr-plugin-xineliboutput-frontend-xine
Obsoletes:	vdr-plugin-xineliboutput-frontend-xine
Provides:	xineliboutput-fe-xine
Obsoletes:	xineliboutput-fe-xine

%description -n xine1.2-xvdr
With this package you can connect to your VDR with xine1.2 with an MRL
like below:
xvdr://127.0.0.1#nocache;demux:mpeg_block

Frontend packages:
- xine-xvdr: Xine frontend
- xine1.2-xvdr: Xine1.2 frontend
- xineliboutput-sxfe: Standalone X11 frontend
- xineliboutput-fbfe: Standalone FB frontend
- xineliboutput-local-sxfe: Local X11 frontend
- xineliboutput-local-fbfe: Local FB frontend

%package -n %plugin-local-sxfe
Group:		Video
Summary:	Local X11 frontend for the xineliboutput VDR plugin
Requires:	xine1.2-xvdr = %version
Requires:	%name = %version
Provides:	vdr-plugin-xineliboutput-frontend-local-x11
Obsoletes:	vdr-plugin-xineliboutput-frontend-local-x11
Provides:	xineliboutput-fe-local-x11
Obsoletes:	xineliboutput-fe-local-x11
Provides:	xineliboutput-fe-x11
Obsoletes:	xineliboutput-fe-x11

%description -n %plugin-local-sxfe
Local X11 frontend for the xineliboutput VDR plugin.

Frontend packages:
- xine-xvdr: Xine frontend
- xine1.2-xvdr: Xine1.2 frontend
- xineliboutput-sxfe: Standalone X11 frontend
- xineliboutput-fbfe: Standalone FB frontend
- xineliboutput-local-sxfe: Local X11 frontend
- xineliboutput-local-fbfe: Local FB frontend

%package -n %plugin-local-fbfe
Group:		Video
Summary:	Local framebuffer/DirectFB frontend for the xineliboutput VDR plugin
Requires:	xine1.2-xvdr = %version
Requires:	%name = %version
Provides:       vdr-plugin-xineliboutput-frontend-local-fb
Obsoletes:      vdr-plugin-xineliboutput-frontend-local-fb
Provides:	xineliboutput-fe-local-fb
Obsoletes:	xineliboutput-fe-local-fb
Provides:	xineliboutput-fe-fb
Obsoletes:	xineliboutput-fe-fb

%description -n %plugin-local-fbfe
Local framebuffer/DirectFB frontend for the xineliboutput VDR
plugin.

Frontend packages:
- xine-xvdr: Xine frontend
- xine1.2-xvdr: Xine1.2 frontend
- xineliboutput-sxfe: Standalone X11 frontend
- xineliboutput-fbfe: Standalone FB frontend
- xineliboutput-local-sxfe: Local X11 frontend
- xineliboutput-local-fbfe: Local FB frontend

%package -n %plugin-sxfe
Group:		Video
Summary:	Standalone X11 frontend for the xineliboutput VDR plugin
Requires:	xine1.2-xvdr = %version
Provides:       vdr-plugin-xineliboutput-frontend-standalone-x11
Obsoletes:      vdr-plugin-xineliboutput-frontend-standalone-x11
Provides:	xineliboutput-fe-standalone-x11
Obsoletes:	xineliboutput-fe-standalone-x11
Provides:	xineliboutput-fe-x11
Obsoletes:	xineliboutput-fe-x11

%description -n %plugin-sxfe
Standalone X11 frontend for the xineliboutput VDR plugin.

Frontend packages:
- xine-xvdr: Xine frontend
- xine1.2-xvdr: Xine1.2 frontend
- xineliboutput-sxfe: Standalone X11 frontend
- xineliboutput-fbfe: Standalone FB frontend
- xineliboutput-local-sxfe: Local X11 frontend
- xineliboutput-local-fbfe: Local FB frontend

%package -n %plugin-fbfe
Group:		Video
Summary:	Standalone framebuffer/DirectFB frontend for the xineliboutput VDR plugin
Requires:	xine1.2-xvdr = %version
Provides:       vdr-plugin-xineliboutput-frontend-standalone-fb
Obsoletes:      vdr-plugin-xineliboutput-frontend-standalone-fb
Provides:	xineliboutput-fe-standalone-fb
Obsoletes:	xineliboutput-fe-standalone-fb
Provides:	xineliboutput-fe-fb
Obsoletes:	xineliboutput-fe-fb

%description -n %plugin-fbfe
Standalone framebuffer/DirectFB frontend for the xineliboutput VDR
plugin.

Frontend packages:
- xine-xvdr: Xine frontend
- xine1.2-xvdr: Xine1.2 frontend
- xineliboutput-sxfe: Standalone X11 frontend
- xineliboutput-fbfe: Standalone FB frontend
- xineliboutput-local-sxfe: Local X11 frontend
- xineliboutput-local-fbfe: Local FB frontend

%prep
%if %snapshot
%setup -q -n vdr-%plugin
%else
%if %prever
%setup -q -n %plugin-%version%prever
%else
%setup -q -n %plugin-%version
%endif
%endif
%autopatch -p1
%vdr_plugin_prep

find -name CVS -type d | while read i; do rm -r "$i" || exit 1; done
perl -pi -e 's,X11R6/lib,X11R6/%{_lib},' Makefile

%vdr_plugin_params_begin %plugin
# Local frontend
# Supported frontends:
# sxfe (X11)
# fbfe (framebuffer)
# none (only remote frontends)
var=LOCAL
param=--local=LOCAL
# Port where to listen for remote clients
# none or 0 disables remote mode
var=REMOTE_PORT
param=--remote=REMOTE_PORT
# Audio driver
# Supported values: auto, alsa, oss, esound, none
var=AUDIO
param=--audio=AUDIO
# Video driver
# Supported values:
# for sxfe: auto, x11, xshm, xv, xvmc, xxmc, vdpau, vidix, sdl, opengl, none
# for fbfe: auto, fb, DirectFB, vidixfb, sdl, dxr3, aadxr3, none
var=VIDEO
param=--video=VIDEO
# Fullscreen mode (X11)
var=FULLSCREEN
param=--fullscreen
# Head Up Display OSD (X11)
var=HUD
param=-D
# Window width
var=WIDTH
param=--width=WIDTH
# Window height
var=HEIGHT
param=--height=HEIGHT
# Use X11 display DISP
var=DISP
param=--display=DISP
# Use xine post plugin POST
# format: pluginname[:arg=val[,arg=val]][,...]
# example: "upmix;tvtime:enabled=1,cheap_mode=1"
var=POST
param=--post=POST
# Force xineliboutput to be primary device when
# there are active frontend(s)
var=PRIMARY
param=--primary
# Exit vdr when local frontend window is closed. You may also want
# to define VDR_MAX_RESTART=0 in /etc/sysconfig/vdr.
var=EXIT_ON_CLOSE
param=--exit-on-close
# Use custom xine-lib config file
var=XINE_LIB_CONFIG
param="-C XINE_LIB_CONFIG"
%vdr_plugin_params_end

mkdir xine-plugins

%build

%vdr_plugin_build VDRINCDIR=%{_includedir}

%install
rm -rf %{buildroot}
%vdr_plugin_install

install -d -m755 %buildroot%xineplugindir/post %buildroot%_bindir

%makeinstall BINDIR=%buildroot%_bindir XINEPLUGINDIR=%buildroot%xineplugindir VDRDIR=.

install -m755 libxineliboutput-*.so.* %{buildroot}%{_vdr_plugin_dir}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%clean
rm -rf %{buildroot}

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY examples

%files -n xine1.2-xvdr
%defattr(-,root,root)
%doc README
# xine-plugins maybe upgraded without new xine-xvdr (while everything still
# works). Therefore we have to include the plugindir as well.
%dir %{xineplugindir}
%{xineplugindir}/*.so
%{xineplugindir}/post/*.so

%files -n %plugin-local-fbfe
%defattr(-,root,root)
%doc README
%dir %{_vdr_plugin_dir}
%{_vdr_plugin_dir}/libxineliboutput-fbfe.so.*

%files -n %plugin-local-sxfe
%defattr(-,root,root)
%doc README
%dir %{_vdr_plugin_dir}
%{_vdr_plugin_dir}/libxineliboutput-sxfe.so.*

%files -n %plugin-fbfe
%defattr(-,root,root)
%doc README
%_bindir/vdr-fbfe

%files -n %plugin-sxfe
%defattr(-,root,root)
%doc README
%_bindir/vdr-sxfe
