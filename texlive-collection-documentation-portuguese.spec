# revision 13822
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-documentation-portuguese
Epoch:		1
Version:	20120224
Release:	1
Summary:	Portuguese documentation
Group:		Publishing
URL:		http://tug.org/texlive
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
