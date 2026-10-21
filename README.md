# NDI Runtime Snap for OBS Studio

This snap provides the proprietary [NDI® SDK](https://ndi.video) runtime library
(`libndi.so`) for OBS Studio plugin snaps that depend on it, such as
[DistroAV](https://github.com/DistroAV/DistroAV).

It is a companion to the **distroav-obs-studio** snap. Both snaps connect to
the [OBS Studio snap](https://snapcraft.io/obs-studio) via the `obs-plugins`
content interface.

## Installation

### Install from the Store

```shell
sudo snap install ndi-runtime
```

### Connect to the OBS Studio snap

```shell
sudo snap connect obs-studio:obs-plugins ndi-runtime:obs-plugins
```

### Pair with DistroAV

```shell
sudo snap install distroav-obs-studio
sudo snap connect obs-studio:obs-plugins distroav-obs-studio:obs-plugins
```

## Architecture

```
obs-studio
  └── obs-plugins:ndi-runtime  →  /ndi-runtime/lib/libndi.so.6
```

The OBS Studio snap's plugin hook automatically adds all mounted plugin `/lib`
directories to `LD_LIBRARY_PATH`, making `libndi.so.6` available to any plugin
that needs it via `dlopen`.

The full NDI SDK license agreement and third-party licenses are bundled in the
snap under `/ndi-runtime/licenses/`.

## License

This snap bundles the **NDI® SDK**, which is proprietary software owned by
Vizrt NDI AB. By using this snap you agree to the terms of the NDI SDK License
Agreement, included in the snap at `/ndi-runtime/licenses/`.

> [!WARNING]
> The binary included in this snap (`libndi.so`) is **proprietary** and is
> governed by Vizrt's license terms — not by any open-source license. This
> snap is provided as a convenience mechanism for distributing the NDI
> runtime to other snapped applications. This is **not legal advice**;
> consult a lawyer if you have concerns about compliance.

NDI® is a registered trademark of Vizrt NDI AB. For more information about NDI,
visit [ndi.video](https://ndi.video/).

## Development

```shell
snapcraft
```

The snap starts in `devel` grade; flip it to `stable` in
`snap/snapcraft.yaml` once the packaged runtime is verified to work.
