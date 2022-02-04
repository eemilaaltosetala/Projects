using System;
using System.Collections.Generic;
using System.Text;

namespace peli
{
    //Luokka Henkilo, joka toteuttaa rajapintaa IOsallistuja
    class Henkilo : IOsallistuja
    {
        //Ominaisuudet, sisältäen rajapinnan toteuttavat ominaisuudet Id ja Nimi
        public int Id { get; set; }
        string Etunimi { get; set; }
        string Sukunimi { get; set; }
        public string Nimi
        {
            get { return $"{Sukunimi} {Etunimi}"; }
            set
            {
                //Splitataan saatu arvo ja jos arvon pituus on 2, niin sijoitetaan arvo[0] Sukunimeksi ja arvo[1] Etunimeksi
                string[] nimi = value.Split();
                if (nimi.Length == 2)
                {
                    Sukunimi = nimi[0];
                    Etunimi = nimi[1];
                }
                else //jos arvo on jokin muu kuin 2
                {
                    throw new Exception("Henkilön nimi on oltava muodossa sukunimi etunimi.");
                }
            }
        }
    }
}
