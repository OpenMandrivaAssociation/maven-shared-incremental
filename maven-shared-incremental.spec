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
BuildRequires:	python
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven


BuildRequires:  maven-shared
BuildRequires:  maven-shared-utils
BuildRequires:  maven-components
BuildRequires:	mvn(com.google.inject:guice-parent:pom::)
BuildRequires:	mvn(org.slf4j:slf4j-parent:pom::)
BuildRequires:	mvn(org.codehaus.plexus:plexus-containers:pom::)

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
# The sources do not import plexus-component-api or the component annotations.
python - <<'PY'
import xml.etree.ElementTree as ET
NS = "http://maven.apache.org/POM/4.0.0"
ET.register_namespace("", NS)

def local(tag):
    return tag.split("}", 1)[-1]

tree = ET.parse("pom.xml")
root = tree.getroot()
drop = {"plexus-component-api", "plexus-component-annotations", "plexus-component-metadata"}
for parent in root.iter():
    for node in list(parent):
        if local(node.tag) not in {"dependency", "plugin"}:
            continue
        artifact = ""
        for child in node:
            if local(child.tag) == "artifactId":
                artifact = (child.text or "").strip()
        if artifact in drop:
            parent.remove(node)
tree.write("pom.xml", encoding="utf-8", xml_declaration=True)
PY

%files -f .mfiles
%doc LICENSE NOTICE

%if %{with javadoc}
%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%endif
