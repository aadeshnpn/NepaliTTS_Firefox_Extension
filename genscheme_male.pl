$file_input = $ARGV[0];
$file_output = $ARGV[1];
$fname = $ARGV[2];
#$file_input = "test.nrm";
#$file_output = "test.scm";
open(fp_in, "< $file_input");
open(fp_out, "> $file_output");
@arrInput = <fp_in>;
close(fp_in);
my $voice = "(voice_mpp_nep_kds_clunits)";
my $play = "(set! u1 (SayText \"@arrInput\"))";
my $save = "(utt.save.wave u1 \"$fname.wav\" \"wav\")";
print fp_out $voice."\n".$play."\n".$save;
#print fp_out $voice."\n".$save;

