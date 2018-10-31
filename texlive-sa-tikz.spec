# revision 32815
# category Package
# catalog-ctan /graphics/pgf/contrib/sa-tikz
# catalog-date 2014-01-29 19:47:58 +0100
# catalog-license lppl1.3
# catalog-version 0.7a
Name:		texlive-sa-tikz
Version:	0.7a
Release:	6
Summary:	TikZ library to draw switching architectures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/sa-tikz
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sa-tikz.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sa-tikz.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
