#Special thanks to GuestAgain on ##electronics for modifying his temperature correction script
#to handle dilution. I touched it up a bit. This is just the bare working version, I will clean
#it up quite a bit and probably make a web version for others to use as well since I could not find one.

#jesus christ what the hell is this? I have no idea what dark arts lay below, but I feel that maybe
#calling out to your diety of choice before executing may be a wise action.. just in case

final_temp = lambda m1, t1, m2, t2: (m1*t1 + m2*t2) / (m1 + m2)
needed_mass = lambda m1, t1, t2, t: m1 * (t1 - t) / (t - t2)
needed_temp = lambda m1, t1, m2, t: t - m1/m2*(t1 - t)
needed_masses = lambda m, t1, t2, t: (m / (1 + (t1 - t) / (t - t2)), m / (1 + (t - t2) / (t1 - t)))
 
#liquids in ounces, setty part before mathy bits
#set variables below
wanted_volume = 4
got_odoban = 0.02
got_ipa = 0.91
wanted_odoban = 0.002
wanted_ipa = 0.60
 
## mathy part below
other_v, odoban_v = needed_masses(wanted_volume, 0, got_odoban, wanted_odoban)
other_c = needed_temp(odoban_v, 0, other_v, wanted_ipa)
water_v, ipa_v = needed_masses(other_v, 0, got_ipa, other_c)
total_v = odoban_v + ipa_v + water_v
#printy part here
print('Total volume:', round(total_v, 2),'Fl.oz')
print('- Odoban:',round(odoban_v,2))
print('- IPA:   ',round(ipa_v,2))
print('- Water: ', round(water_v,2))
print('Concentrations:')
#print('- Odoban:', odoban_v*got_odoban/total_v)
print('( - Odoban: '+"{:.2%}".format(odoban_v*got_odoban/total_v));
#print('- IPA:', ipa_v*got_ipa/total_v)
print('( - IPA:    '+"{:.2%}".format(ipa_v*got_ipa/total_v));

#pretty printy bits below. no looking, WIP.

#let's try to clean up some of this math to handle the formatting easier.
#this seems to work, might integrate it further but for now, formatting is good enough
#after initial cleanup. May add commandline to specify the required volume,
#current iso percentage, wanted iso percentage.
odoban_start = round(odoban_v,2)
odoban_end = odoban_v*got_odoban/total_v
iso_start = round(ipa_v,2)
iso_end = round(ipa_v*got_ipa/total_v,2)
water = round(water_v,2)
volume = round(total_v, 2)
#print('Total Volume ', volume, 'oz')