%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name childprocess


Summary: A simple and reliable gem for controlling external programs
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.5.3
Release: 2%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/jarib/childprocess
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(ffi)
#BuildRequires: %{?scl_prefix}rubygem(ffi)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
#BuildRequires: %{?scl_prefix_ror}rubygem(rspec) >= 2.0.0
#BuildRequires: %{?scl_prefix}rubygem(coveralls)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
This gem aims at being a simple and reliable solution for controlling external
programs running in the background on any Ruby / OS combination.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/
rm -f %{buildroot}%{gem_instdir}/.document %{buildroot}%{gem_instdir}/.gitignore
rm -f %{buildroot}%{gem_instdir}/.rspec %{buildroot}%{gem_instdir}/Rakefile
rm -f %{buildroot}%{gem_instdir}/.travis.yml
rm -f %{buildroot}%{gem_instdir}/childprocess.gemspec
rm -f %{buildroot}%{gem_instdir}/Gemfile
chmod 644 %{buildroot}%{gem_libdir}/childprocess/jruby/process.rb
chmod 644 %{buildroot}%{gem_libdir}/childprocess/windows/process.rb
chmod 644 %{buildroot}%{gem_instdir}/spec/*.rb

# coveralls not in scl
#%%check
#pushd .%{gem_instdir}
#%%{?scl:scl enable %{scl} - << \EOF}
#rspec spec
#%%{?scl:EOF}
#popd

%files
%doc %{gem_instdir}/LICENSE
%{gem_libdir}
%dir %{gem_instdir}
%{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_instdir}/README.md
%{gem_instdir}/spec
%doc %doc %{gem_docdir}

%changelog
* Thu Oct 16 2014 Josef Stribny <jstribny@redhat.com> - 0.5.3-2
- Add SCL macros

* Thu Aug 28 2014 Josef Stribny <jstribny@redhat.com> - 0.5.3-1
- Update childprocess to version 0.5.3

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 23 2013 Mo Morsi <mmorsi@redhat.com> - 0.3.9-1
- Update to childprocess 0.3.9

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 20 2013 Vít Ondruch <vondruch@redhat.com> - 0.3.6-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 13 2012 Mo Morsi <mmorsi@redhat.com> - 0.3.6-1
- Update to childprocess 0.3.6

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 03 2012 Vít Ondruch <vondruch@redhat.com> - 0.2.0-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 03 2011 Chris Lalancette <clalance@redhat.com> - 0.2.0-1
- Initial package
