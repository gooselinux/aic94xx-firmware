Name:		aic94xx-firmware
Summary:	Adaptec SAS 44300, 48300, 58300 Sequencer Firmware for AIC94xx driver
Version:	30
Release:	2%{?dist}
License:	Redistributable, no modification permitted
Group:		System Environment/Kernel
Source0:	http://download.adaptec.com/scsi/linux/aic94xx-seq-%{version}-1.tar.gz
# Copied from:
# http://www.adaptec.com/AdaptecCom/Templates/driverdetail.aspx?NRMODE=Published&NRNODEGUID={35B611BC-9789-4B5B-82C6-85A2CCA8A46A}&NRORIGINALURL=%2fen-US%2fspeed%2fscsi%2flinux%2faic94xx-seq-30-1_tar_gz.htm&NRCACHEHINT=Guest
Source1:	LICENSE.aic94xx
URL:		http://www.adaptec.com/en-US/speed/scsi/linux/aic94xx-seq-30-1_tar_gz.htm
Requires:	udev
BuildArch:	noarch

%description
Adaptec SAS 44300, 48300, 58300 Sequencer Firmware for Open-Source AIC94xx 
Driver.

%prep
%setup -q -c
cp %{SOURCE1} .
%{_bindir}/rpm2cpio aic94xx_seq-30-1.noarch.rpm | cpio -idv
chmod +r lib/firmware/aic94xx-seq.fw
chmod -x README-94xx.pdf

%build
# Firmware, do nothing.

%install
mkdir -p %{buildroot}/lib/firmware/
install -m0644 lib/firmware/aic94xx-seq.fw %{buildroot}/lib/firmware/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE.aic94xx README-94xx.pdf
/lib/firmware/aic94xx-seq.fw

%changelog
* Mon Mar 15 2010 Tom "spot" Callaway <tcallawa@redhat.com> 30-1
- Initial package
