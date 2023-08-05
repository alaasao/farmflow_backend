# Generated by Django 4.2.4 on 2023-08-05 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_likes_number_like_card'),
        ('products', '0007_product_productimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('payment', models.DecimalField(decimal_places=2, max_digits=5)),
                ('wilaya', models.CharField(blank=True, choices=[('Adrar', 'Adrar'), ('Chlef', 'Chlef'), ('Laghouat', 'Laghouat'), ('Oum El Bouaghi', 'Oum El Bouaghi'), ('Batna', 'Batna'), ('Bejaia', 'Bejaia'), ('Biskra', 'Biskra'), ('Bechar', 'Bechar'), ('Blida', 'Blida'), ('Bouira', 'Bouira'), ('Tamanrasset', 'Tamanrasset'), ('Tebessa', 'Tebessa'), ('Tlemcen', 'Tlemcen'), ('Tiaret', 'Tiaret'), ('Tizi Ouzou', 'Tizi Ouzou'), ('Alger', 'Alger'), ('Djelfa', 'Djelfa'), ('Jijel', 'Jijel'), ('Setif', 'Setif'), ('Saida', 'Saida'), ('Skikda', 'Skikda'), ('Sidi Bel Abbes', 'Sidi Bel Abbes'), ('Annaba', 'Annaba'), ('Guelma', 'Guelma'), ('Constantine', 'Constantine'), ('Medea', 'Medea'), ('Mostaganem', 'Mostaganem'), ('MSila', 'MSila'), ('Mascara', 'Mascara'), ('Ouargla', 'Ouargla'), ('Oran', 'Oran'), ('El Bayadh', 'El Bayadh'), ('Illizi', 'Illizi'), ('Bordj Bou Arreridj', 'Bordj Bou Arreridj'), ('Boumerdes', 'Boumerdes'), ('El Tarf', 'El Tarf'), ('Tindouf', 'Tindouf'), ('Tissemsilt', 'Tissemsilt'), ('El Oued', 'El Oued'), ('Khenchela', 'Khenchela'), ('Souk Ahras', 'Souk Ahras'), ('Tipaza', 'Tipaza'), ('Mila', 'Mila'), ('Ain Defla', 'Ain Defla'), ('Naama', 'Naama'), ('Ain Temouchent', 'Ain Temouchent'), ('Ghardaia', 'Ghardaia'), ('Relizane', 'Relizane')], max_length=50, null=True)),
                ('baladiya', models.CharField(blank=True, choices=[['Abadla', 'Abadla'], ['Abi Youcef', 'Abi Youcef'], ['Achaacha', 'Achaacha'], ['Adrar', 'Adrar'], ['Aflou', 'Aflou'], ['Aghbalou', 'Aghbalou'], ['Agouni Gueghrane', 'Agouni Gueghrane'], ['Ahl El Ksar', 'Ahl El Ksar'], ['Ahmar El Ain', 'Ahmar El Ain'], ['Ain Abessa', 'Ain Abessa'], ['Ain Adden', 'Ain Adden'], ['Ain Azel', 'Ain Azel'], ['Ain Beida', 'Ain Beida'], ['Ain Beida Harriche', 'Ain Beida Harriche'], ['Ain Benian', 'Ain Benian'], ['Ain Ben Khelil', 'Ain Ben Khelil'], ['Ain Bouchekif', 'Ain Bouchekif'], ['Ain Boucif', 'Ain Boucif'], ['Ain Bouihi', 'Ain Bouihi'], ['Ain Bya', 'Ain Bya'], ['Ain Defla', 'Ain Defla'], ['Ain Djasser', 'Ain Djasser'], ['Ain El Assel', 'Ain El Assel'], ['Ain El Berda', 'Ain El Berda'], ['Ain El Fakroun', 'Ain El Fakroun'], ['Ain El Hadjar', 'Ain El Hadjar'], ['Ain El Hadjel', 'Ain El Hadjel'], ['Ain El Ibel', 'Ain El Ibel'], ['Ain El Kercha', 'Ain El Kercha'], ['Ain El Orak', 'Ain El Orak'], ['Ain Fares', 'Ain Fares'], ['Ain Fekan', 'Ain Fekan'], ['Ain Ferah', 'Ain Ferah'], ['Ain Fezza', 'Ain Fezza'], ['Ain Ghoraba', 'Ain Ghoraba'], ['Ain Kada', 'Ain Kada'], ['Ain Kechra', 'Ain Kechra'], ['Ain Kerma', 'Ain Kerma'], ['Ain Khadra', 'Ain Khadra'], ['Ain Lahdjar', 'Ain Lahdjar'], ['Ain Larbi', 'Ain Larbi'], ['Ain Legraj', 'Ain Legraj'], ['Ain Madhi', 'Ain Madhi'], ['Ain Mellouk', 'Ain Mellouk'], ["Ain M'lila", "Ain M'lila"], ['Ain Nehala', 'Ain Nehala'], ['Ain Ou Ksir', 'Ain Ou Ksir'], ['Ain Oussera', 'Ain Oussera'], ['Ain Reggada', 'Ain Reggada'], ['Ain Roua', 'Ain Roua'], ['Ain Sefra', 'Ain Sefra'], ['Ain Sekhouna', 'Ain Sekhouna'], ['Ain Smara', 'Ain Smara'], ['Ain Soltane', 'Ain Soltane'], ['Ain Soltane', 'Ain Soltane'], ['Ain Tagourait', 'Ain Tagourait'], ['Ain Tarik', 'Ain Tarik'], ['Ain Tedles', 'Ain Tedles'], ['Ain Tesra', 'Ain Tesra'], ['Ain Tindamine', 'Ain Tindamine'], ['Ain Tolba', 'Ain Tolba'], ['Ain Touila', 'Ain Touila'], ['Ain TurK', 'Ain TurK'], ['Ain Yagout', 'Ain Yagout'], ['Ain Zaatout', 'Ain Zaatout'], ['Ain Zaouia', 'Ain Zaouia'], ['Ain Zerga', 'Ain Zerga'], ['Ain Zouit', 'Ain Zouit'], ['Ait Aggouacha', 'Ait Aggouacha'], ['Ait Boumahdi', 'Ait Boumahdi'], ['Ait Khelili', 'Ait Khelili'], ['Ait Mahmoud', 'Ait Mahmoud'], ['Ait Oumalou', 'Ait Oumalou'], ['Ait Smail', 'Ait Smail'], ['Ait Toudert', 'Ait Toudert'], ['Ait Yahia Moussa', 'Ait Yahia Moussa'], ['Akbil', 'Akbil'], ['Akerrou', 'Akerrou'], ['Alaimia', 'Alaimia'], ['Amalou', 'Amalou'], ['Amieur', 'Amieur'], ['Amizour', 'Amizour'], ['Ammari', 'Ammari'], ['Amoucha', 'Amoucha'], ['Annaba', 'Annaba'], ['Aomar', 'Aomar'], ['Aouf', 'Aouf'], ['Aoulef', 'Aoulef'], ['Arib', 'Arib'], ['Arzew', 'Arzew'], ['Assela', 'Assela'], ['Ath Mansour Taourirt', 'Ath Mansour Taourirt'], ['Azazga', 'Azazga'], ['Azzaba', 'Azzaba'], ['Azziz', 'Azziz'], ['Baata', 'Baata'], ['Babar', 'Babar'], ['Bab El Oued', 'Bab El Oued'], ['Babor', 'Babor'], ['Badredine El Mokrani', 'Badredine El Mokrani'], ['Baghlia', 'Baghlia'], ['Baraki', 'Baraki'], ['Barika', 'Barika'], ['Batna', 'Batna'], ['Bazer-Sakra', 'Bazer-Sakra'], ['Bechloul', 'Bechloul'], ['Beidha Bordj', 'Beidha Bordj'], ['Bekkaria', 'Bekkaria'], ['Belaas', 'Belaas'], ['Belaiba', 'Belaiba'], ['Belarbi', 'Belarbi'], ['Belkheir', 'Belkheir'], ['Benabdelmalek Ramdane', 'Benabdelmalek Ramdane'], ['Benaicha Chelia', 'Benaicha Chelia'], ['Ben Aknoun', 'Ben Aknoun'], ['Ben Azzouz', 'Ben Azzouz'], ['Ben Badis', 'Ben Badis'], ['Ben Choud', 'Ben Choud'], ['Bendaoud', 'Bendaoud'], ['Ben Freha', 'Ben Freha'], ['Benhar', 'Benhar'], ['Beni Aissi', 'Beni Aissi'], ['Benian', 'Benian'], ['Beni Bahdel', 'Beni Bahdel'], ['Beni Bouattab', 'Beni Bouattab'], ['Beni Chaib', 'Beni Chaib'], ['Beni Dejllil', 'Beni Dejllil'], ['Beni-Douala', 'Beni-Douala'], ['Beni Foudala El Hakania', 'Beni Foudala El Hakania'], ['Beni Haoua', 'Beni Haoua'], ['Beni Ilmane', 'Beni Ilmane'], ['Beni Lahcene', 'Beni Lahcene'], ['Beni-Mellikeche', 'Beni-Mellikeche'], ['Beni Messous', 'Beni Messous'], ['Beni Mezline', 'Beni Mezline'], ['Beni-Mouhli', 'Beni-Mouhli'], ['Beni-Ouartilane', 'Beni-Ouartilane'], ['Beni Ounif', 'Beni Ounif'], ['Beni Rached', 'Beni Rached'], ['Beni Saf', 'Beni Saf'], ['Beni Smiel', 'Beni Smiel'], ['Beni-Tamou', 'Beni-Tamou'], ['Beni Zentis', 'Beni Zentis'], ['Beni-Zikki', 'Beni-Zikki'], ['Benkhelil', 'Benkhelil'], ['Bennasser Benchohra', 'Bennasser Benchohra'], ['Ben Srour', 'Ben Srour'], ['Benyahia Abderrahmane', 'Benyahia Abderrahmane'], ['Berbacha', 'Berbacha'], ['Berrahal', 'Berrahal'], ['Berriche', 'Berriche'], ['Berrouaghia', 'Berrouaghia'], ['Besbes', 'Besbes'], ['Bhir El Chergui', 'Bhir El Chergui'], ['Bir Ben Laabed', 'Bir Ben Laabed'], ['Bir Chouhada', 'Bir Chouhada'], ['Bir-El-Arch', 'Bir-El-Arch'], ['Bir El Djir', 'Bir El Djir'], ['Bir Foda', 'Bir Foda'], ['Bir Haddada', 'Bir Haddada'], ['Bir Kasdali', 'Bir Kasdali'], ['Bir Mokkadem', 'Bir Mokkadem'], ['Bir Ould Khelifa', 'Bir Ould Khelifa'], ['Biskra', 'Biskra'], ['Blida', 'Blida'], ['Bologhine Ibnou Ziri', 'Bologhine Ibnou Ziri'], ['Bordj Ben Azzouz', 'Bordj Ben Azzouz'], ['Bordj Bounaama', 'Bordj Bounaama'], ['Bordj El Emir Abdelkader', 'Bordj El Emir Abdelkader'], ['Bordj El Kiffan', 'Bordj El Kiffan'], ['Bordj Ghdir', 'Bordj Ghdir'], ['Bordj Okhriss', 'Bordj Okhriss'], ['Bordj Sebbat', 'Bordj Sebbat'], ['Bordj Zemoura', 'Bordj Zemoura'], ['Bouaiche', 'Bouaiche'], ['Boualem', 'Boualem'], ['Bouati Mahmoud', 'Bouati Mahmoud'], ['Bouchakroune', 'Bouchakroune'], ['Boucherahil', 'Boucherahil'], ['Bouda', 'Bouda'], ['Boudjebaa El Bordj', 'Boudjebaa El Bordj'], ['Boudjeriou Messaoud', 'Boudjeriou Messaoud'], ['Boudouaou', 'Boudouaou'], ['Boudria Beniyadjis', 'Boudria Beniyadjis'], ['Boufatis', 'Boufatis'], ['Bougara', 'Bougara'], ['Boughezoul', 'Boughezoul'], ['Bougtoub', 'Bougtoub'], ['Bouguirat', 'Bouguirat'], ['Bouhadjar', 'Bouhadjar'], ['Bouhamza', 'Bouhamza'], ['Bou Haroun', 'Bou Haroun'], ['Bou Henni', 'Bou Henni'], ['Bouhmama', 'Bouhmama'], ['Bouinan', 'Bouinan'], ['Bouira Lahdab', 'Bouira Lahdab'], ['Boukadir', 'Boukadir'], ['Boukhadra', 'Boukhadra'], ['Boukhlifa', 'Boukhlifa'], ['Boulhaf Dyr', 'Boulhaf Dyr'], ['Boumagueur', 'Boumagueur'], ['Boumahra Ahmed', 'Boumahra Ahmed'], ['Boumia', 'Boumia'], ['Bounoura', 'Bounoura'], ['Bouraoui Belhadef', 'Bouraoui Belhadef'], ['Bourouba', 'Bourouba'], ['Bousfer', 'Bousfer'], ['Bousselam', 'Bousselam'], ['Boussif Ouled Askeur', 'Boussif Ouled Askeur'], ['Bouteldja', 'Bouteldja'], ['Boutlelis', 'Boutlelis'], ['Bou Zedjar', 'Bou Zedjar'], ['Bouzeguene', 'Bouzeguene'], ['Bouzina', 'Bouzina'], ['Breira', 'Breira'], ['Brida', 'Brida'], ['Chaabet El Ham', 'Chaabet El Ham'], ['Challalat El Adhaoura', 'Challalat El Adhaoura'], ['Chahbounia', 'Chahbounia'], ['Chaiba', 'Chaiba'], ['Charouine', 'Charouine'], ['Chebli', 'Chebli'], ['Chefia', 'Chefia'], ['Chehaima', 'Chehaima'], ['Chelghoum Laid', 'Chelghoum Laid'], ['Chellal', 'Chellal'], ['Chemini', 'Chemini'], ['Cheniguel', 'Cheniguel'], ['Cheraga', 'Cheraga'], ['Cherchel', 'Cherchel'], ['Chetma', 'Chetma'], ['Chetouane Belaila', 'Chetouane Belaila'], ['Chiffa', 'Chiffa'], ['Chihani', 'Chihani'], ['Chlef', 'Chlef'], ['Chorfa', 'Chorfa'], ['Chouaiba (Ouled Rahma)', 'Chouaiba (Ouled Rahma)'], ['Chrea', 'Chrea'], ['Collo', 'Collo'], ['Corso', 'Corso'], ['Dahouara', 'Dahouara'], ['Damiat', 'Damiat'], ['Daoussen', 'Daoussen'], ['Dar Chioukh', 'Dar Chioukh'], ['Darguina', 'Darguina'], ['Debdeb', 'Debdeb'], ['Dechmia', 'Dechmia'], ['Dehamcha', 'Dehamcha'], ['Deldoul', 'Deldoul'], ['Dely Ibrahim', 'Dely Ibrahim'], ['Derrag', 'Derrag'], ['Dhaya', 'Dhaya'], ['Didouche Mourad', 'Didouche Mourad'], ['Djaafra', 'Djaafra'], ['Djamora', 'Djamora'], ['Djasr Kasentina', 'Djasr Kasentina'], ['Djebahia', 'Djebahia'], ['Djebala El Khemissi', 'Djebala El Khemissi'], ['Djebel Messaad', 'Djebel Messaad'], ['Djelfa', 'Djelfa'], ['Djellal', 'Djellal'], ['Djemaa Ouled Cheikh', 'Djemaa Ouled Cheikh'], ['Djemila', 'Djemila'], ['Djendel Saadi Mohamed', 'Djendel Saadi Mohamed'], ['Djerma', 'Djerma'], ['Djidiouia', 'Djidiouia'], ['Djinet', 'Djinet'], ['Douaouda', 'Douaouda'], ['Douera', 'Douera'], ['Doui Thabet', 'Doui Thabet'], ['Draa El Caid', 'Draa El Caid'], ['Draa-Kebila', 'Draa-Kebila'], ['Draria', 'Draria'], ['Drean', 'Drean'], ['El Abadia', 'El Abadia'], ['El Achir', 'El Achir'], ['El Adjiba', 'El Adjiba'], ['El Aioun (Algeria)', 'El Aioun (Algeria)'], ['El Amiria', 'El Amiria'], ['El Amria', 'El Amria'], ['El Ançar', 'El Ançar'], ['El Aouana', 'El Aouana'], ['El Aricha', 'El Aricha'], ['El Assafia', 'El Assafia'], ['El Atteuf', 'El Atteuf'], ['El Bayadh', 'El Bayadh'], ['El Biar', 'El Biar'], ['El Biodh Sidi Cheikh', 'El Biodh Sidi Cheikh'], ['El Bordj', 'El Bordj'], ['El Bouni', 'El Bouni'], ['El Dhaala', 'El Dhaala'], ['El Eulma', 'El Eulma'], ['El Fedjoudj', 'El Fedjoudj'], ['El Fehoul', 'El Fehoul'], ['El Flaye', 'El Flaye'], ['El Ghedir', 'El Ghedir'], ['El Ghomri', 'El Ghomri'], ['El Gor', 'El Gor'], ['El Guelb El Kebir', 'El Guelb El Kebir'], ['El Guettana', 'El Guettana'], ['El Hacaiba', 'El Hacaiba'], ['El Hachimia', 'El Hachimia'], ['El Hadjab', 'El Hadjab'], ['El Hadjar', 'El Hadjar'], ['El Hakimia', 'El Hakimia'], ['El Hamdania', 'El Hamdania'], ['El Hamma', 'El Hamma'], ['El Haouaita', 'El Haouaita'], ['El Harmilia', 'El Harmilia'], ['El Harrouch', 'El Harrouch'], ['El Hassasna', 'El Hassasna'], ['El Hassi', 'El Hassi'], ['El Houamed', 'El Houamed'], ['El Idrissia', 'El Idrissia'], ['El Kala', 'El Kala'], ['El Kennar Nouchfi', 'El Kennar Nouchfi'], ['El Kerma', 'El Kerma'], ['El Khabouzia', 'El Khabouzia'], ['El Kheither', 'El Kheither'], ['El Kheng', 'El Kheng'], ['El Kouif', 'El Kouif'], ['El Madania', 'El Madania'], ['El Magharia', 'El Magharia'], ['El Main', 'El Main'], ['El Malabiodh', 'El Malabiodh'], ['El Mamounia', 'El Mamounia'], ['El Marsa', 'El Marsa'], ['El Matmor', 'El Matmor'], ['El Mehara', 'El Mehara'], ['El Meniaa', 'El Meniaa'], ['El Messaid', 'El Messaid'], ["El M'Ghair", "El M'Ghair"], ['El Milia', 'El Milia'], ['El Mokrani (El Madjen)', 'El Mokrani (El Madjen)'], ['El Ogla, El Oued Province', 'El Ogla, El Oued Province'], ['El Ouata', 'El Ouata'], ['El Oueldja', 'El Oueldja'], ['El Ouitaya', 'El Ouitaya'], ['El-Ouldja', 'El-Ouldja'], ['El Ouricia', 'El Ouricia'], ['El Tarf', 'El Tarf'], ['Emir Abdelkader', 'Emir Abdelkader'], ['Emjez Edchich', 'Emjez Edchich'], ['Erg Ferradj', 'Erg Ferradj'], ['Es Sebt', 'Es Sebt'], ['Faidh El Botma', 'Faidh El Botma'], ['Fellaoucene', 'Fellaoucene'], ['Fenoughil', 'Fenoughil'], ['Ferdjioua', 'Ferdjioua'], ['Ferraguig', 'Ferraguig'], ['Filfila', 'Filfila'], ['Foggaret Azzouia', 'Foggaret Azzouia'], ['Foughala', 'Foughala'], ['Foum Toub', 'Foum Toub'], ['Frenda', 'Frenda'], ['Froha', 'Froha'], ['Ghardaia', 'Ghardaia'], ['Ghassoul', 'Ghassoul'], ['Ghebala', 'Ghebala'], ['Ghessira', 'Ghessira'], ['Ghriss', 'Ghriss'], ['Gouraya', 'Gouraya'], ['Guelal Boutaleb', 'Guelal Boutaleb'], ['Gueltat Sidi Saad', 'Gueltat Sidi Saad'], ['Guemar', 'Guemar'], ['Guerdjoum', 'Guerdjoum'], ['Guerrouma', 'Guerrouma'], ['Guettara', 'Guettara'], ['Guiga', 'Guiga'], ['Hacine', 'Hacine'], ['Had Echkalla', 'Had Echkalla'], ['Hadjera Zerga', 'Hadjera Zerga'], ['Hadjout', 'Hadjout'], ['Had Sahary', 'Had Sahary'], ['Hamadia', 'Hamadia'], ['Hamala', 'Hamala'], ['Hamma Bouziane', 'Hamma Bouziane'], ['Hammam Ben Salah', 'Hammam Ben Salah'], ['Hammam Bouhadjar', 'Hammam Bouhadjar'], ['Hammam Debagh', 'Hammam Debagh'], ['Hammam Guergour', 'Hammam Guergour'], ["Hammam N'Bail", "Hammam N'Bail"], ['Hammam Soukhna', 'Hammam Soukhna'], ['Hamri', 'Hamri'], ['Hanencha', 'Hanencha'], ['Haraoua', 'Haraoua'], ['Harbil', 'Harbil'], ['Hasnaoua', 'Hasnaoua'], ['Hassani Abdelkrim', 'Hassani Abdelkrim'], ['Hassi Bahbah', 'Hassi Bahbah'], ['Hassi Ben Okba', 'Hassi Ben Okba'], ['Hassi Dahou', 'Hassi Dahou'], ['Hassi El Euch', 'Hassi El Euch'], ['Hassi Fedoul', 'Hassi Fedoul'], ['Hassi Gara', 'Hassi Gara'], ['Hassi Mameche', 'Hassi Mameche'], ['Hassi Messaoud', 'Hassi Messaoud'], ['Hassi Zehana', 'Hassi Zehana'], ['Helliopolis', 'Helliopolis'], ['Herenfa', 'Herenfa'], ['Hoceinia', 'Hoceinia'], ['Hounet', 'Hounet'], ['Hydra', 'Hydra'], ['Iboudraren', 'Iboudraren'], ['Idjeur', 'Idjeur'], ['Iferhounene', 'Iferhounene'], ['Iflissen', 'Iflissen'], ['Ighrem', 'Ighrem'], ['Illilten', 'Illilten'], ['Illoula Oumalou', 'Illoula Oumalou'], ['In Amenas', 'In Amenas'], ['In Guezzam', 'In Guezzam'], ['Inoughissen', 'Inoughissen'], ['In Zghmir', 'In Zghmir'], ['Issers', 'Issers'], ['Kadiria', 'Kadiria'], ['Kalaa', 'Kalaa'], ['Kanoua', 'Kanoua'], ['Kef El Ahmar', 'Kef El Ahmar'], ['Kendira', 'Kendira'], ['Kerzaz', 'Kerzaz'], ['Khalouia', 'Khalouia'], ['Khatouti Sed Eldjir', 'Khatouti Sed Eldjir'], ['Kheiredine', 'Kheiredine'], ['Khelil', 'Khelil'], ['Khemis Miliana', 'Khemis Miliana'], ['Khemisti', 'Khemisti'], ['Khenchela', 'Khenchela'], ['Khenguet Sidi Nadji', 'Khenguet Sidi Nadji'], ['Khezzara', 'Khezzara'], ['Khoubana', 'Khoubana'], ['Kimmel', 'Kimmel'], ['Kouas', 'Kouas'], ['Kouinine', 'Kouinine'], ['Ksabi', 'Ksabi'], ['Ksar Chellala', 'Ksar Chellala'], ['Ksar El Boukhari', 'Ksar El Boukhari'], ['Ksar Hirane', 'Ksar Hirane'], ['Ksour', 'Ksour'], ['Lac Des Oiseaux', 'Lac Des Oiseaux'], ['Lahlef', 'Lahlef'], ['Lakhdaria', 'Lakhdaria'], ['Larbaa', 'Larbaa'], ['Larbaa-Nath-Irathen', 'Larbaa-Nath-Irathen'], ['Lardjem', 'Lardjem'], ['Layoune', 'Layoune'], ['Lazrou', 'Lazrou'], ['Lemsane', 'Lemsane'], ['Les Eucalyptus', 'Les Eucalyptus'], ['Lioua', 'Lioua'], ['Maadid', 'Maadid'], ['Maala', 'Maala'], ['Maamora', 'Maamora'], ['Maarif', 'Maarif'], ['Machroha', 'Machroha'], ['Maghnia', 'Maghnia'], ['Magrane', 'Magrane'], ['Mahdia', 'Mahdia'], ['Makhda', 'Makhda'], ['Makouda', 'Makouda'], ['Mansoura', 'Mansoura'], ['Mansourah', 'Mansourah'], ['Maoussa', 'Maoussa'], ["Marsa Ben M'Hidi", "Marsa Ben M'Hidi"], ['Mascara', 'Mascara'], ["M'Chedallah", "M'Chedallah"], ["M'Cif", "M'Cif"], ["M'Doukal", "M'Doukal"], ['Mechouneche', 'Mechouneche'], ['Mechraa Safa', 'Mechraa Safa'], ['Medjana', 'Medjana'], ['Medjaz Sfa', 'Medjaz Sfa'], ['Medjedel', 'Medjedel'], ['Medroussa', 'Medroussa'], ['Meftaha', 'Meftaha'], ['Megheraoua', 'Megheraoua'], ['Mekhadma', 'Mekhadma'], ['Mekkedra', 'Mekkedra'], ['Melaab', 'Melaab'], ['Mellakou', 'Mellakou'], ['Menaa (Ouled Atia)', 'Menaa (Ouled Atia)'], ['Mendes', 'Mendes'], ['Merahna', 'Merahna'], ['Merhoum', 'Merhoum'], ['Merine', 'Merine'], ['Mers El Kebir', 'Mers El Kebir'], ['Mesra', 'Mesra'], ['Messelmoun', 'Messelmoun'], ['Metlili', 'Metlili'], ['Mezdour', 'Mezdour'], ['Mezghrane', 'Mezghrane'], ["M'Hamid", "M'Hamid"], ['Mihoub', 'Mihoub'], ['Miliana', 'Miliana'], ['Misserghin', 'Misserghin'], ["M'Kira", "M'Kira"], ["M'Liliha", "M'Liliha"], ['Mogheul', 'Mogheul'], ['Mohamed Belouizdad', 'Mohamed Belouizdad'], ['Mohammedia', 'Mohammedia'], ['Morsot', 'Morsot'], ['Moudjebara', 'Moudjebara'], ['Moulay Slissen', 'Moulay Slissen'], ['Mouzaia', 'Mouzaia'], ["M'Sara", "M'Sara"], ['Msirda Fouaga', 'Msirda Fouaga'], ["M'Tarfa", "M'Tarfa"], ['Mustafa Ben Brahim', 'Mustafa Ben Brahim'], ['Naciria', 'Naciria'], ['Nadorah', 'Nadorah'], ['Nakhla', 'Nakhla'], ['Nedroma', 'Nedroma'], ['Nekmaria', 'Nekmaria'], ['Nezla', 'Nezla'], ["N'Goussa", "N'Goussa"], ['Ogla Melha', 'Ogla Melha'], ['Ouacif', 'Ouacif'], ['Ouaguenoun', 'Ouaguenoun'], ['Ouanougha', 'Ouanougha'], ['Ouarizane', 'Ouarizane'], ['Oued Athmenia', 'Oued Athmenia'], ['Oued Chaaba', 'Oued Chaaba'], ['Oued Chorfa', 'Oued Chorfa'], ['Oued Djemaa', 'Oued Djemaa'], ['Oued El Abtal', 'Oued El Abtal'], ['Oued El Alleug', 'Oued El Alleug'], ['Oued El Barad', 'Oued El Barad'], ['Oued El Djemaa', 'Oued El Djemaa'], ['Oued El Ma', 'Oued El Ma'], ['Oued Essalem', 'Oued Essalem'], ['Oued Fragha', 'Oued Fragha'], ['Oued Goussine', 'Oued Goussine'], ['Oued Kebrit', 'Oued Kebrit'], ['Oued Lilli', 'Oued Lilli'], ["Oued M'Zi", "Oued M'Zi"], ['Oued Rhiou', 'Oued Rhiou'], ['Oued Sebbah', 'Oued Sebbah'], ['Oued Seguen', 'Oued Seguen'], ['Oued Smar', 'Oued Smar'], ['Oued Taourira', 'Oued Taourira'], ['Oued Tlelat', 'Oued Tlelat'], ['Oued Zhour', 'Oued Zhour'], ['Ouenza', 'Ouenza'], ['Ouled Abbes', 'Ouled Abbes'], ['Ouled Addouane', 'Ouled Addouane'], ['Ouled Aissa', 'Ouled Aissa'], ['Ouled Ammar', 'Ouled Ammar'], ['Ouled Aouf', 'Ouled Aouf'], ['Ouled Ben Abdelkader', 'Ouled Ben Abdelkader'], ['Ouled Bouachra', 'Ouled Bouachra'], ['Ouled Boughalem', 'Ouled Boughalem'], ['Ouled Brahim', 'Ouled Brahim'], ['Ouled Chebel', 'Ouled Chebel'], ['Ouled Daid', 'Ouled Daid'], ['Ouled Djellal', 'Ouled Djellal'], ['Ouled Fadhel', 'Ouled Fadhel'], ['Ouled Fayet', 'Ouled Fayet'], ['Ouled Hamla', 'Ouled Hamla'], ['Ouled Hedadj', 'Ouled Hedadj'], ['Ouled Khaled', 'Ouled Khaled'], ['Ouled Khoudir', 'Ouled Khoudir'], ['Ouled Maalah', 'Ouled Maalah'], ['Ouled Madhi', 'Ouled Madhi'], ['Ouled Mimoun', 'Ouled Mimoun'], ['Ouled Moussa', 'Ouled Moussa'], ['Ouled Rached', 'Ouled Rached'], ['Ouled Rechache', 'Ouled Rechache'], ['Ouled Saber', 'Ouled Saber'], ['Ouled Sellem', 'Ouled Sellem'], ['Ouled Sidi Brahim', 'Ouled Sidi Brahim'], ['Ouled Sidi Mihoub', 'Ouled Sidi Mihoub'], ['Ouled Slama', 'Ouled Slama'], ['Ouled Tebben', 'Ouled Tebben'], ['Ouled Yaich', 'Ouled Yaich'], ['Ouled Zaoui', 'Ouled Zaoui'], ['Oultene', 'Oultene'], ['Oum Ali', 'Oum Ali'], ['Oum El Adhaim', 'Oum El Adhaim'], ['Oum El Bouaghi', 'Oum El Bouaghi'], ['Oum Laadham', 'Oum Laadham'], ['Oum Touyour', 'Oum Touyour'], ['Ourmes', 'Ourmes'], ['Ouzzelaguen', 'Ouzzelaguen'], ['Ragouba', 'Ragouba'], ['Rahouia', 'Rahouia'], ['Ramdane Djamel', 'Ramdane Djamel'], ['Raml Souk', 'Raml Souk'], ['Ras Ain Amirouche', 'Ras Ain Amirouche'], ['Ras El Aioun', 'Ras El Aioun'], ['Ras El Oued', 'Ras El Oued'], ['Rechaiga', 'Rechaiga'], ['Reggane', 'Reggane'], ['Reguiba', 'Reguiba'], ['Relizane', 'Relizane'], ['Remila', 'Remila'], ['Robbah', 'Robbah'], ['Roknia', 'Roknia'], ['Rouached', 'Rouached'], ['Rouiba', 'Rouiba'], ['Rouissat', 'Rouissat'], ['Safel El Ouiden', 'Safel El Ouiden'], ['Saf Saf El Ouesra', 'Saf Saf El Ouesra'], ['Saida', 'Saida'], ['Salah Bouchaour', 'Salah Bouchaour'], ['Saneg', 'Saneg'], ['Sayada', 'Sayada'], ['Sebaine', 'Sebaine'], ['Sebdou', 'Sebdou'], ['Sebseb', 'Sebseb'], ['Seddouk', 'Seddouk'], ['Sed Rahal', 'Sed Rahal'], ['Sedraya', 'Sedraya'], ['Seggana', 'Seggana'], ['Sehailia', 'Sehailia'], ['Selaoua Announa', 'Selaoua Announa'], ['Selmana', 'Selmana'], ['Seraidi', 'Seraidi'], ['Serghine', 'Serghine'], ['Setif', 'Setif'], ['Sfisef', 'Sfisef'], ['Si Abdelghani', 'Si Abdelghani'], ['Sidi Abdeldjebar', 'Sidi Abdeldjebar'], ['Sidi Abdelmoumene', 'Sidi Abdelmoumene'], ['Sidi Abderrahmane', 'Sidi Abderrahmane'], ['Sidi Ahmed', 'Sidi Ahmed'], ['Sidi Aissa', 'Sidi Aissa'], ['Sidi Ali', 'Sidi Ali'], ['Sidi Ali Boussidi', 'Sidi Ali Boussidi'], ['Sidi Amar', 'Sidi Amar'], ['Sidi Amar', 'Sidi Amar'], ['Sidi Ameur', 'Sidi Ameur'], ['Sidi Aoun', 'Sidi Aoun'], ['Sidi Baizid', 'Sidi Baizid'], ['Sidi Bel Abbes', 'Sidi Bel Abbes'], ['Sidi Ben Adda', 'Sidi Ben Adda'], ['Sidi Boubekeur', 'Sidi Boubekeur'], ['Sidi Boussaid', 'Sidi Boussaid'], ['Sidi Bouzid', 'Sidi Bouzid'], ['Sidi Chahmi', 'Sidi Chahmi'], ['Sidi Dahou Zair', 'Sidi Dahou Zair'], ['Sidi Daoud', 'Sidi Daoud'], ['Sidi Embarek', 'Sidi Embarek'], ['Sidi Ghiles', 'Sidi Ghiles'], ['Sidi Hamadouche', 'Sidi Hamadouche'], ['Sidi Kada', 'Sidi Kada'], ['Sidi Khaled', 'Sidi Khaled'], ['Sidi Khelil', 'Sidi Khelil'], ['Sidi Khouiled', 'Sidi Khouiled'], ['Sidi Lahcene', 'Sidi Lahcene'], ['Sidi Lakhdar', 'Sidi Lakhdar'], ['Sidi Lazreg', 'Sidi Lazreg'], ['Sidi Marouf', 'Sidi Marouf'], ['Sidi Merouane', 'Sidi Merouane'], ["Sidi M'Hamed", "Sidi M'Hamed"], ["Sidi M'Hamed Benali", "Sidi M'Hamed Benali"], ['Sidi Moussa', 'Sidi Moussa'], ['Sidi Naamane', 'Sidi Naamane'], ['Sidi Ouriache (Tadmaya)', 'Sidi Ouriache (Tadmaya)'], ['Sidi Rached', 'Sidi Rached'], ['Sidi Safi', 'Sidi Safi'], ['Sidi Slimane', 'Sidi Slimane'], ['Sidi Slimane', 'Sidi Slimane'], ['Sidi Yacoub', 'Sidi Yacoub'], ['Sidi Ziane', 'Sidi Ziane'], ['Sig', 'Sig'], ['Si Mustapha', 'Si Mustapha'], ['Skikda', 'Skikda'], ['Smaoun', 'Smaoun'], ['Souaflia', 'Souaflia'], ['Souahlia', 'Souahlia'], ['Souamaa', 'Souamaa'], ['Souarekh', 'Souarekh'], ['Souhan', 'Souhan'], ['Souk Ahras', 'Souk Ahras'], ['Souk El Had', 'Souk El Had'], ['Souk El Tenine', 'Souk El Tenine'], ['Souk Naamane', 'Souk Naamane'], ['Souk Tleta', 'Souk Tleta'], ['Sour', 'Sour'], ['Stah Guentis', 'Stah Guentis'], ['Stidia', 'Stidia'], ['Stitten', 'Stitten'], ['Tabia', 'Tabia'], ['Tacheta Zegagha', 'Tacheta Zegagha'], ['Tadjemout', 'Tadjemout'], ['Tadjenanet', 'Tadjenanet'], ['Tadmait', 'Tadmait'], ['Tafissour', 'Tafissour'], ['Tafraout', 'Tafraout'], ['Tagdemt', 'Tagdemt'], ['Taghlimet', 'Taghlimet'], ['Taghzout', 'Taghzout'], ['Taguedit', 'Taguedit'], ['Taibet', 'Taibet'], ['Tala Hamza', 'Tala Hamza'], ['Taleb Larbi', 'Taleb Larbi'], ['Talmine', 'Talmine'], ['Tamantit', 'Tamantit'], ['Tamelaht', 'Tamelaht'], ['Tamest', 'Tamest'], ['Tamlouka', 'Tamlouka'], ['Tamridjet', 'Tamridjet'], ['Tamtert', 'Tamtert'], ['Tamzoura', 'Tamzoura'], ['Taoudmout', 'Taoudmout'], ['Taoura', 'Taoura'], ['Taourit Ighil', 'Taourit Ighil'], ['Tarik Ibn-Ziad', 'Tarik Ibn-Ziad'], ['Taskriout', 'Taskriout'], ['Tassala', 'Tassala'], ['Taya', 'Taya'], ['Tazmalt', 'Tazmalt'], ['Tazrouk', 'Tazrouk'], ['Tebessa', 'Tebessa'], ['Telagh', 'Telagh'], ['Teleghma', 'Teleghma'], ['Tenedla', 'Tenedla'], ['Teniet El Abed', 'Teniet El Abed'], ['Tenira', 'Tenira'], ['Terny Beni Hediel', 'Terny Beni Hediel'], ['Terrai Bainnane', 'Terrai Bainnane'], ['Tessala-El-Merdja', 'Tessala-El-Merdja'], ['Texenna', 'Texenna'], ['Thenia', 'Thenia'], ['Thleth Douair', 'Thleth Douair'], ['Tiaret', 'Tiaret'], ['Tiberguent', 'Tiberguent'], ['Tichy', 'Tichy'], ['Tidjelabine', 'Tidjelabine'], ['Tifra', 'Tifra'], ['Tigharghar', 'Tigharghar'], ['Tigzirt', 'Tigzirt'], ['Tilmouni', 'Tilmouni'], ['Timezrit', 'Timezrit'], ['Timiaouine', 'Timiaouine'], ['Timmimoun', 'Timmimoun'], ['Tindouf', 'Tindouf'], ['Tinerkouk', 'Tinerkouk'], ['Tiout', 'Tiout'], ['Tircine', 'Tircine'], ['Tissemsilt', 'Tissemsilt'], ['Tixter', 'Tixter'], ['Tizi Ghenif', 'Tizi Ghenif'], ["Tizi-N'Berber", "Tizi-N'Berber"], ['Tizi Ouzou', 'Tizi Ouzou'], ['T Kout', 'T Kout'], ['Tolga', 'Tolga'], ['Toudja', 'Toudja'], ['Tousmouline', 'Tousmouline'], ['Treat', 'Treat'], ['Tsabit', 'Tsabit'], ['Yahia Beniguecha', 'Yahia Beniguecha'], ['Yatafene', 'Yatafene'], ['Youb', 'Youb'], ['Zaarouria', 'Zaarouria'], ['Zahana', 'Zahana'], ['Zaouia El Abidia', 'Zaouia El Abidia'], ['Zarzour', 'Zarzour'], ['Zeboudja', 'Zeboudja'], ['Zeghaia', 'Zeghaia'], ['Zelfana', 'Zelfana'], ['Zemmouri', 'Zemmouri'], ['Zeralda', 'Zeralda'], ['Zeribet El Oued', 'Zeribet El Oued'], ['Zerouala', 'Zerouala'], ['Zighoud Youcef', 'Zighoud Youcef'], ['Zitouna', 'Zitouna'], ['Zorg', 'Zorg'], ['Zoubiria', 'Zoubiria']], max_length=50, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
    ]
