# revision 13822
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-documentation-portuguese
Epoch:		1
Version:	20120224
Release:	11
Summary:	Portuguese documentation
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-documentation-portuguese.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-beamer-tut-pt
Requires:	texlive-cursolatex
Requires:	texlive-latexcheat-ptbr
Requires:	texlive-lshort-portuguese
Requires:	texlive-xypic-tut-pt
Requires:	texlive-collection-documentation-base

%description
TeXLive collection-documentation-portuguese package.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install


%changelog
* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780250
- Update to latest release.
- Import texlive-collection-documentation-portuguese
- Import texlive-collection-documentation-portuguese

