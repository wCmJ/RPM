Name:       hello-world
Version:    1
Release:    1
Summary:    Most simple RPM package
License:    FIXME

%description
This is my first RPM package, which does nothing.

%prep
# we have no source, so nothing here

%build
cat > hello-world.sh << EOF
#!/usr/bin/bash
echo hello world
EOF

%install
mkdir -p %{buildroot}/urs/bin/
install -m 755 hello-world.sh %{buildroot}/usr/bin/hello-world.sh

%files
/usr/bin/hello-world.sh

%changelog
# let skip this for now

----------------------------------------------------------------
rpmdev-setuptree
rpmbuild -ba hello-world.spec

you will get *.rpm which is your first RPM package, it can be installed in the system and tested.

