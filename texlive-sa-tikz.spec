%global tl_name sa-tikz
%global tl_revision 32815

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7a
Release:	%{tl_revision}.1
Summary:	TikZ library to draw switching architectures
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/sa-tikz
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sa-tikz.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sa-tikz.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a library that offers an easy way to draw switching
architectures and to customize their aspect.

