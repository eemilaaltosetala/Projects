using System;
using System.Collections.Generic;
using System.Text;
using static System.Console;

namespace peli
{
    //staattinen luokka Sovellus
    static class Sovellus
    {
        //staattinen Random-olio
        static Random rnd = new Random();

        //staattinen metodi, joka tekee yksilö-kilpailun
        static void TeeYksiloKilpailu(double min, double max)
        {
            //kysytään nimeä ja luetaan käyttäjän syöte, syötettä käytetään nimenä, kun tehdään uusi yksilökilpailu
            Write("Anna yksilökilpailun nimi: ");
            string yksiloKilpailunNimi = ReadLine();
            YksiloKilpailu<Henkilo, double> yksiloKilpailu = new YksiloKilpailu<Henkilo, double>()
            {
                Nimi = yksiloKilpailunNimi
            };

            do
            {
                Write("Anna osallistujan nimi muodossa \"sukunimi etunimi\" (tyhjä lopettaa): ");
                string syote = ReadLine();

                if (syote.Length == 0) //jos syötteen pituus on 0, katkaistaan looppi
                {
                    break;
                }

                //lisätään Suoritukset listaan uusi olio, jolle annetaan osallistujana uusi henkilö-olio, jolle annetaan nimi sekä...
                yksiloKilpailu.Suoritukset.Add(new Suoritus<Henkilo, double>
                {
                    Osallistuja = new Henkilo()
                    {
                        Nimi = syote
                    },
                    Tulos = min + rnd.NextDouble() * (max - min) //... tulos, joka arvotaan käyttäen apuna Random-oliota
                });
            } while (true);

            //tulostetaan tyhjä rivi, muutetaan teksti keltaiseksi, sekä käydään Suoritukset-listaa läpi, tulostaen pyydetyt asiat
            WriteLine();
            ForegroundColor = ConsoleColor.Yellow;
            WriteLine($"Kilpailun {yksiloKilpailunNimi} tulokset:");
            foreach (var item in yksiloKilpailu.Suoritukset)
            {
                WriteLine($"{item.Osallistuja.Nimi}, {Math.Round(item.Tulos, 2)}"); //tässä tapauksessa osallistujan nimi sekä tulos 2 desimaalin tarkkuudella
            }
            ResetColor(); //muutetaan väri takaisin
            WriteLine();

        }

        //staattinen metodi, joka tekee joukkue-kilpailun
        static void TeeJoukkueKilpailu(int maxpisteet)
        {
            //kysytään nimeä ja luetaan käyttäjän syöte, syötettä käytetään nimenä, kun tehdään uusi joukkuekilpailu
            Write("Anna joukkuekilpailun nimi: ");
            string joukkueKilpailunNimi = ReadLine();
            JoukkueKilpailu<Joukkue, int> joukkueKilpailu = new JoukkueKilpailu<Joukkue, int>()
            {
                Nimi = joukkueKilpailunNimi
            };

            string syote;

            do
            {

                Write("Anna osallistujan nimi (tyhjä lopettaa): ");
                syote = ReadLine();

                if (syote.Length == 0) //katkaisee loopin kun annetaan tyhjä syöte
                {
                    break;
                }

                //lisätään Suoritukset listaan uusi olio, jolle annetaan osallistujana uusi henkilö-olio, jolle annetaan nimi sekä...
                joukkueKilpailu.Suoritukset.Add(new Suoritus<Joukkue, int>
                {
                    Osallistuja = new Joukkue()
                    {
                        Nimi = syote
                    },
                    Tulos = rnd.Next(0, maxpisteet) //... tulos, joka arvotaan käyttäen apuna Random-oliota
                });

            } while (true);

            //tulostetaan tyhjä rivi, muutetaan teksti keltaiseksi, sekä käydään Suoritukset-listaa läpi, tulostaen pyydetyt asiat
            WriteLine();
            ForegroundColor = ConsoleColor.Yellow;
            WriteLine($"Kilpailun {joukkueKilpailunNimi} tulokset:");
            foreach (var item in joukkueKilpailu.Suoritukset)
            {
                WriteLine($"{item.Osallistuja.Nimi}, {item.Tulos} pistettä"); //osallistujan nimi sekä tulos
            }
            ResetColor();
            WriteLine();
        }

        //opettajan antamat metodit, tätä kutsutaan desimaalilukupakottaen metodista, tällä siis palautetaan desimaali
        static double Desimaaliluku(string kehote, int tarkkuus = -1)
        {
            double paluu;
            Write($"{kehote} ");
            if (!double.TryParse(ReadLine(), out paluu)) //tarkistaa, onko annettu syöte desimaali, jos ei, heittää virheen, jos on, palauttaa arvon
            {
                throw new ApplicationException("Syöte ei ole kelvollinen desimaaliluku.");
            }
            return tarkkuus >= 0 ? Math.Round(paluu, tarkkuus) : paluu;
        }
        //tätä kutsutaan aja-ohjelmassa, vikasietoinen desimaaliluvun pyyntö
        static double DesimaalilukuPakottaen(string kehote, int tarkkuus = -1)
        {
            do
            {
                try
                {
                    return Desimaaliluku(kehote, tarkkuus);
                }
                catch (Exception e)
                {
                    WriteLine(e.Message);
                }
            } while (true);
        }
        //tätä kutsutaan kokonaislukupakottaen metodista, tällä palautetaan kokonaisluku
        static int Kokonaisluku(string kehote, int min = int.MinValue, int max = int.MaxValue)
        {
            int paluu;
            Write($"{kehote} ");
            if (!int.TryParse(ReadLine(), out paluu) || (paluu < min || paluu > max)) //tarkistetaan onko syöte kelvollinen kokonaisluku, jos ei heittää virheen, jos on palauttaa arvon
            {
                throw new ApplicationException("Syöte ei ole kelvollinen kokonaisluku." +
                    (min > int.MinValue ? ($" Minimi on {min}.") : "") +
                    (max < int.MaxValue ? ($" Maksimi on {max}.") : ""));
            }
            return paluu;
        }
        //tätä kutsutaan aja-ohjelmassa, vikasietoinen kokonaisluvun pyyntö
        static int KokonaislukuPakottaen(string kehote, int min = int.MinValue, int max =
        int.MaxValue)
        {
            do
            {
                try
                {
                    return Kokonaisluku(kehote, min, max);
                }
                catch (Exception e)
                {
                    WriteLine(e.Message);
                }
            } while (true);
        }

        //staattinen metodi aja, jossa kysytään käyttäjältä millainen kilpailu tehdään ja kutsutaan vastauksen perusteella pisteitä antavia metodeja
        //desimaali- ja kokonaislukupakottaen sekä kutsutaan TeeYksiloKilpailu tai TeeJoukkueKilpailu metodeja
        //tätä tehdään kunnes annetaan tyhjä
        public static void Aja()
        {
            do
            {
                Write("Tehdäänkö yksilö- (y) vai joukkuekilpailu (j), tyhjä lopettaa: ");
                string syote = ReadLine();

                if (syote.Length == 0)
                {
                    break;
                }
                else if (syote == "y")
                {

                    double minimi = DesimaalilukuPakottaen("Anna yksilökilapilun minimitulos: ");
                    double maksimi = DesimaalilukuPakottaen("Anna yksilökilapilun maksimitulos: ");
                    TeeYksiloKilpailu(minimi, maksimi);
                }
                else if (syote == "j")
                {
                    int maksimi = KokonaislukuPakottaen("Anna joukkuekilpailun maksimipistemäärä: ");
                    TeeJoukkueKilpailu(maksimi);
                }



            } while (true);
        }
    }
}
