using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class MainMenu : MonoBehaviour
{
    public Animator transitions;
    public bool shop;

    void Start()
    {
        transitions = GetComponent<Animator>();
    }

    public void Transition()
    {
        shop = transitions.GetBool("ShopOpen");
        transitions.SetBool("ShopOpen", !shop);
    }

    public void StartGame()
    {
        SceneManager.LoadScene("TheFirstGame");
    }
}
