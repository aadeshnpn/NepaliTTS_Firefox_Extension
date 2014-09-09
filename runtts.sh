#echo "Running scripts from Python Wrapper"
fname=$1
appmainpath="/usr/lib/cgi-bin/tts/"
apptextpath="/usr/lib/cgi-bin/tts/inputtext"
appfilename="/usr/lib/cgi-bin/tts/inputtext/$fname"
cd $appmainpath
perl utf82It3.pl "$fname.txt" "$fname.it3" Nepali_PhoneSet.txt
#echo "conversion to it3 complete"
perl normalize.pl "$fname.it3" "$fname.nrm"
perl genscheme_male.pl "$fname.nrm" "$fname.scm" "$fname"
#echo "normalization done"
cp -f "$fname.scm" ./ver16/mpp_nep_kds/
cd ./ver16/mpp_nep_kds/
festival festvox/mpp_nep_kds_clunits.scm -b "$fname.scm"
avconv -i "$fname.wav" -map 0:a -b 128K "$fname.mp3"
cp -f "$fname.mp3" /var/www/html/tts/wav/
mv "$fname.mp3" "$fname.scm" "$fname.wav" $apptextpath
cd $appmainpath
mv "$fname.txt" "$fname.it3" "$fname.nrm" "$fname.scm" $apptextpath
#cd $appmainpath
#mv $fname* $apptextpath
#cp -f tts_out.wav /svr/http/tts/wav/
