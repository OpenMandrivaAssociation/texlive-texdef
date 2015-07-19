# revision 26420
# category Package
# catalog-ctan /support/texdef
# catalog-date 2012-05-15 15:44:48 +0200
# catalog-license gpl3
# catalog-version 1.7b
Name:		texlive-texdef
Version:	1.7b
Release:	9
Summary:	Display the definitions of TeX commands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/texdef
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texdef.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texdef.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texdef.source.tar.xz
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
%{_texmfdistdir}/scripts/texdef/texdef.pl
%doc %{_texmfdistdir}/doc/support/texdef/INSTALL
%doc %{_texmfdistdir}/doc/support/texdef/README
%doc %{_texmfdistdir}/doc/support/texdef/texdef.pdf
#- source
%doc %{_texmfdistdir}/source/support/texdef/texdef.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/texdef/texdef.pl texdef
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.7b-1
+ Revision: 812893
- Update to latest release.

* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.6-1
+ Revision: 805104
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.4-2
+ Revision: 756601
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.4-1
+ Revision: 719679
- texlive-texdef
- texlive-texdef
- texlive-texdef

