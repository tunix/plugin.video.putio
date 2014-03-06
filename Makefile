all: zip 
zip:
	zip -vr ../plugin.video.putiov2-0.0.3.zip . -x *.git* *.idea*
