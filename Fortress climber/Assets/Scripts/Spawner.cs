using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Spawner : MonoBehaviour
{
    private Vector2 coord;
    private float time = 0;
    private float coinTime = 0;
    private float springTime = 0;
    private float slowmoTime = 0;
    private float spikeTime = 0;
    private float shieldTime = 0;
    private bool warn = false;

    public GameObject coin;//done
    public GameObject spike;//done
    public GameObject slowmo;//done
    public GameObject shield;//done
    public GameObject spring;//done

    public GameObject warning;

    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    private void Update()
    {
        if(warn)
        time += Time.deltaTime;
        coinTime += Time.deltaTime;
        springTime += Time.deltaTime;
        slowmoTime += Time.deltaTime;
        spikeTime += Time.deltaTime;
        shieldTime += Time.deltaTime;


        if (coinTime > 5)
        {
            coinTime = 0;
            Instantiate(coin, new Vector3(Random.Range(-14f, 14f), Random.Range(-9f, 1f), 0f), Quaternion.identity);
        }
        if (springTime > 8)
        {
            springTime = 0;
            Instantiate(spring, new Vector3(Random.Range(-14f, 14.5f), -11.5f, 0f), Quaternion.identity);
        }
        if (slowmoTime > 15)
        {
            slowmoTime = 0;
            Instantiate(slowmo, new Vector3(Random.Range(-14f, 14.5f), Random.Range(-9f, 0f), 0f), Quaternion.identity);
        }
        if (shieldTime > 20)
        {
            shieldTime = 0;
            Instantiate(shield, new Vector3(Random.Range(-14f, 14.5f), -10f, 0f), Quaternion.identity);
        }
        if (spikeTime > 8)
        {
            warn = true;
            coord = new Vector2(Random.Range(-14f, 14.5f), Random.Range(-14f, 14.5f));
            Instantiate(warning, new Vector3(coord.x, -10f, 0f), Quaternion.identity);
            Instantiate(warning, new Vector3(coord.y, -10f, 0f), Quaternion.identity);
            spikeTime = 0;
        }
        if (time > 2)
        {
            warn = false;
            Instantiate(spike, new Vector3(coord.x, -11.5f, 0f), Quaternion.identity);
            Instantiate(spike, new Vector3(coord.y, -11.5f, 0f), Quaternion.identity);
            time = 0f;
        }
    }
}
