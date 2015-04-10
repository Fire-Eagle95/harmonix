#!/usr/bin/perl

	local ($buffer, @pairs, $pair, $name, $value, %FORM);
	$ENV{'REQUEST_METHOD'} =~ tr/a-z/A-Z/;
	if ($ENV{'REQUEST_METHOD'} eq "GET")
	{
		$buffer = $ENV{'QUERY_STRING'};
	}
	@pairs = split(/&/, $buffer);
	foreach $pair (@pairs)
	{
		($name, $value) = split(/=/, $pair);
		$value =~ tr/+/ /;
		$value =~ s/%(..)/pack("C", hex($1))/eg;
		$FORM{$name} = $value;
	}
	my $name = $FORM{name};
	my $username = $FORM{username};
	my $psswd = $FORM{psswd};
my $filename = 'members.csv';
open(my $fh, '<:encoding(UTF-8)', $filename);
my $boolean = 0;
my $space = ' ';
if(index($name,$space) != -1) 
{
	$boolean = 1;
}
elsif(index($username,$space) != -1) 
{
	$boolean = 1;
} 
elsif(index($psswd,$space) != -1) {
	$boolean = 1;
}
while(my $row = <$fh>)
{
	chomp $row;
	($a, $b, $c) = split(/ /, $row);
	if ($b eq  $username)
	{
		$boolean = 1;
	}
}
close $fh;
print "Content-type:text/html\r\n\r\n";
if($boolean == 1){
print '<html>';
print '<head>';
print '<title>Registration failed</title>';
print '</head>';
print '<body bgcolor="A9F5F2" text="#08088A"><h2>We are sorry but a member already has this username or you tried to  input a space</h2>';
print '<a href="http://cgi.cs.mcgill.ca/~pgianf/become_member.html">Try to register again</a><br/><br/>';
print '<a href="http://cgi.cs.mcgill.ca/~pgianf/welcome.html">Go back to Home page</a>';
}
else {
print '<html>';
print '<head>';
print '<title>Registration was successful</title>';
print '</head>';
print '<body bgcolor="A9F5F2" text="#08088A"><h2>Your registration was successful! Congratulations</h2>';
print "Your name is $name<br/>";
print "Your username is $username<br/>";
print "Your password is $psswd<br/><br/>";
print '<a href="http://cgi.cs.mcgill.ca/~pgianf/welcome.html">Go back to Home page</a>';
print '</body>';
print '</html>';
open(my $fh, '>>', $filename);
print $fh "$name $username $psswd\n";
close $fh;
}
exit 0;

