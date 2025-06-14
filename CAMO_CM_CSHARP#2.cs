using System;

public class DatabaseManager
{
    public void SavePersonInfo(string name, string surname, string address)
    {
        try
        {
            Console.WriteLine($"Kişi bilgileri kaydediliyor: {name}, {surname}, {address}");
        }
        catch (Exception ex)
        {
            Console.WriteLine("Hata: " + ex.Message);
        }
    }
}

class Program
{
    static void Main()
    {
        DatabaseManager dbManager = new DatabaseManager();
        dbManager.SavePersonInfo("Ad", "Soyad", "Adres");
    }
}