## What's Going On?

There's are a couple of things at play here.

1. I do not code sign my app as I don't want to (nor feel a need to) pay for a certificate for an open source app that anyone can just read through the code of and build themselves if they'd like. Releasing it as an EXE is a convenience, not a necessity.
2. Anti-Virus' (AVs) pick up a lot of repeated patterns. In this case, I'm freezing the code into an EXE using [Pyinstaller](https://pyinstaller.org/en/stable/), and since this is available to anyone, there's a lot of bad actors that also freeze their code using Pyinstaller. As AVs use repeated patterns for detection, there can and WILL be instances of it being picked up as a virus.

## GitHub Issues Opened About This

Any issues opened on this repo about this will be closed by me with the link to this explanation posted in them. As I explained above, if you'd like to use the app but don't trust the EXE, please read through the source and build it yourself. Me providing an EXE is a convenience, not a necessity.

## VirusTotal Links Per Release

- [1.0.0](https://virustotal.com/gui/file/5fd745d211abd9d4a79d1c6d6c8491b50dd1f54009867997092cc9d626a25a30)
- [1.1.0](https://virustotal.com/gui/file/eb1493adff0a1cb8e05db9376128bed7a07e7d32be9325ec771d05b7b8ec2924)
- [1.2.4](https://virustotal.com/gui/file/a337e80ba59e6fa20c33973eda59010e7748b1ae7595066b41992478178f2aaa)
