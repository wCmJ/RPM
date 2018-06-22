Summary: {string}
%define version
Name: {string}

%prep      //defines the commands necessary to prepare for the build.
%setup -q

%build    //contains the commands to build the software. Usually, this will include just a few commands, since most of the real instrctions appear in the Makefile.
./configure CXXFLAGS=-O3 --prefix=$RPM_BUILD_ROOT/usr

%install
%{__rm} -rf $RPM_BUILD_ROOT

%clean    //cleans up the files that the commands in the other sections create
%{__rm} -rf $RPM_BUILD_ROOT

%files    //lists the files to go into the binary RPM, along with the defined file attributes.
%defattr(-, root, root)
or %defattr(0755, root, root, 0755)











