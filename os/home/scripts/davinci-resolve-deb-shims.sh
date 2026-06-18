#!/usr/bin/env bash
# Build and install metadata-only shim packages so the DaVinci Resolve installer's
# dependency check passes on Ubuntu 24.04. The check looks for the pre-t64 names
# (libapr1, libaprutil1, libasound2, libglib2.0-0), which Noble renamed to *t64.
# Each shim just registers the old name and depends on the t64 package; no library
# files are created or modified.
set -euo pipefail

declare -A shims=(
    [libapr1]=libapr1t64
    [libaprutil1]=libaprutil1t64
    [libasound2]=libasound2t64
    [libglib2.0-0]=libglib2.0-0t64
)

build_dir=$(mktemp -d)
trap 'rm -rf "$build_dir"' EXIT

for name in "${!shims[@]}"; do
    real=${shims[$name]}
    version=$(dpkg-query -W -f='${Version}' "$real")
    pkg_dir="$build_dir/$name"
    mkdir -p "$pkg_dir/DEBIAN"
    cat > "$pkg_dir/DEBIAN/control" <<EOF
Package: $name
Version: $version
Architecture: amd64
Maintainer: local <root@localhost>
Depends: $real
Section: libs
Priority: optional
Description: Transitional shim mapping $name to $real (Ubuntu 24.04 t64 transition)
EOF
    dpkg-deb --build --root-owner-group "$pkg_dir" "$build_dir/$name.deb" >/dev/null
done

sudo dpkg -i "$build_dir"/*.deb
