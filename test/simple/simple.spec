Summary:       Nothing
Name:          simple
Version:       0.0.0
Release:       1%{?dist}

License:       MIT
URL:           https://github.com/jw3/mock-rpm-action

%description
Testing the mock-rpm-action

%prep

%build
echo %{version} > %{name}
chmod +x %{name}

%install
install -D simple-command %{buildroot}/%{_bindir}/%{name}

%check

%files
%attr(755,root,root) %{_bindir}/%{name}

%changelog
* Tue Dec 12 2023 John Wass <jwass3@gmail.com> 0.0.0-1
- Inception
