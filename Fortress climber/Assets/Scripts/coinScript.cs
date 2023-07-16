using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class coinScript : MonoBehaviour
{
    public bool coinPicked = false;
    private float time;

    private void Start()
    {

    }

    // Update is called once per frame
    private void Update()
    {
        time += Time.deltaTime;
        if (time > 3)
        {
            Destroy(gameObject);
        }

    }

    private void OnTriggerEnter2D(Collider2D col)
    {
        if (col.gameObject.CompareTag("player"))
        {
            Destroy(gameObject);
            coinPicked = true;
        }

    }

}
