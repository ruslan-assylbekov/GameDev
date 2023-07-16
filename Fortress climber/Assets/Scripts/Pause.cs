using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Pause : MonoBehaviour
{
    public void PauseGame()
    {
        Time.timeScale = 0f;
    }
    public void UnPause()
    {
        Time.timeScale = 1f;
    }
    public void GoToMenu()
    {
        SceneManager.LoadScene("MainMenu");
    }
}
