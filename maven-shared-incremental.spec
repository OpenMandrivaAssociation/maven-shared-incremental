%bcond_with javadoc
Name:           maven-shared-incremental
Version:        1.1
Release:        5.3
Group:	Development/Java
Summary:        Maven Incremental Build support utilities
License:        ASL 2.0

URL:            https://maven.apache.org/shared/maven-shared-incremental/
Source0:        http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildArch:      noarch
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven


BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-api)

%description
Various utility classes and plexus components for supporting
incremental build functionality in maven plugins.

%if %{with javadoc}
%package javadoc
Summary:          API documentation for %{name}


%endif
%if %{with javadoc}
%description javadoc
This package provides %{summary}.

%endif
%prep
%setup -q

%files -f .mfiles
%doc LICENSE NOTICE

%if %{with javadoc}
%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%endif
