Name:		texlive-texdef
Version:	64967
Release:	2
Summary:	Display the definitions of TeX commands
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/texdef
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texdef.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texdef.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texdef.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-texdef.bin = %{EVRD}

%description
The (Perl) script displays the definition of (La)TeX command
sequences/macros. Various options allow the selection of the
used class and package files and other things which can have
influence on the definition (before/after the preamble, inside
an environment, ...). The script creates a temporary TeX file
which is then compiled using (La)TeX to find the '\meaning' of
the command sequence. The result is formatted and presented to
the user. Length or number command sequences (dimensions,
\char..., count registers, ...) are recognized and the
contained value is also shown (using \the). Special definitions
like protected macros are also recognized and the underlying
macros are shown as well. The script will show plain TeX
definitions by default. LaTeX and ConTeXt are supported,
including flavours (pdf(la)tex, lua(la)tex, xe(la)tex, ...).
The flavour can be selected using an command line option or
over the script name: latexdef will use LaTeX as default, etc.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/texdef
%{_texmfdistdir}/scripts/texdef
%doc %{_texmfdistdir}/doc/support/texdef
#- source
%doc %{_texmfdistdir}/source/support/texdef

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/texdef/texdef.pl texdef
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
