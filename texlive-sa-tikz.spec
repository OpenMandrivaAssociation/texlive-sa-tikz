Name:		texlive-sa-tikz
Version:	32815
Release:	1
Summary:	TikZ library to draw switching architectures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/sa-tikz
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sa-tikz.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sa-tikz.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a library that offers an easy way to draw
switching architectures and to customize their aspect.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sa-tikz/sa-tikz.sty
%{_texmfdistdir}/tex/latex/sa-tikz/tikzlibraryswitching-architectures.code.tex
%doc %{_texmfdistdir}/doc/latex/sa-tikz/README
%doc %{_texmfdistdir}/doc/latex/sa-tikz/pgfmanual-en-macros.tex
%doc %{_texmfdistdir}/doc/latex/sa-tikz/sa-tikz-doc.pdf
%doc %{_texmfdistdir}/doc/latex/sa-tikz/sa-tikz-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
