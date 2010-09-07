#!/usr/bin/env ruby

require 'benchmark'
require 'net/http'
require 'uri'

def callURI(baseurl,name,rows,index)
  uri = sprintf("http://%s/%s/%d/%d",baseurl,name,rows,index)
  url = URI.parse(uri)
  req = Net::HTTP::Get.new(url.path)
  res = Net::HTTP.start(url.host,url.port) do |http|
    http.request(req)
  end
  return res.kind_of? Net::HTTPOK
end

def runTest(n,rows)
  baseURI = 'localhost:8082'
  initResults()
  1.upto(n) do |index|
    $results.each_pair do |k,v|
      success = nil
      rez = Benchmark.realtime { success = callURI(baseURI,k,rows,index) }
      if success
        $results[k][:time] += rez
        $results[k][:success] += 1 
      else
        $results[k][:failed] += 1
      end
      $results[k][:average] = $results[k][:time]/$results[k][:success]
    end
  end
  best = 1
  printf("Overhead %d:\n",rows)
  $results.each_value.sort_by { |v| v[:average] }.each_with_index do |v,i|
    k = $results.index(v)
    rank = 0
    if i == 0
      rank = 1
      best = v[:average]
    else
      rank = v[:average] / best
    end
    $results[k][:total] += rank
    $results[k][:exectime] += $results[k][:time]
    printf("%25s: | %d total, %d failed | %7.3fs overall, %.3fs each | score: %7.3f |\n", v[:name], v[:success]+v[:failed], v[:failed], v[:time], v[:average], rank)
  end
  print("\n\n")
end
  
def initResults()
  $results.each_key do |k|
    $results[k][:time] = 0.0
    $results[k][:average] = 0.0
    $results[k][:success] = 0
    $results[k][:failed] = 0
  end
end

$results = {
  'bottlesimpletemplate' => {:exectime => 0.0, :total => 0.0, :name => "bottle w/SimpleTemplate"},
  'bottlebreve' => {:exectime => 0.0, :total => 0.0, :name => "bottle w/Breve"},
  'bottledjango' => {:exectime => 0.0, :total => 0.0, :name => "bottle w/Django"},
  'bottlejinja' => {:exectime => 0.0, :total => 0.0, :name => "bottle w/Jinja"},
  'bottlemako' => {:exectime => 0.0, :total => 0.0, :name => "bottle w/Mako"},
  'bottletenjin' => {:exectime => 0.0, :total => 0.0, :name => "bottle w/Tenjin"},
  'bottletemplator' => {:exectime => 0.0, :total => 0.0, :name => "bottle w/Templator"},
  'webappbreve' => {:exectime => 0.0, :total => 0.0, :name => "webapp w/Breve"},
  'webappmako' => {:exectime => 0.0, :total => 0.0, :name => "webapp w/Mako"},
  'webappdjango' => {:exectime => 0.0, :total => 0.0, :name => "webapp w/Django"},
  'webappjinja' => {:exectime => 0.0, :total => 0.0, :name => "webapp w/Jinja"},
  'webappsimpletemplate' => {:exectime => 0.0, :total => 0.0, :name => "webapp w/SimpleTemplate"},
  'webapptenjin' => {:exectime => 0.0, :total => 0.0, :name => "webapp w/Tenjin"},
  'webapptemplator' => {:exectime => 0.0, :total => 0.0, :name => "webapp w/Templator"},
  'webpytemplator' => {:exectime => 0.0, :total => 0.0, :name => "web.py w/Templator"},
  'web2breve' => {:exectime => 0.0, :total => 0.0, :name => "webapp2 w/Breve"},
  'web2mako' => {:exectime => 0.0, :total => 0.0, :name => "webapp2 w/Mako"},
  'web2django' => {:exectime => 0.0, :total => 0.0, :name => "webapp2 w/Django"},
  'web2jinja' => {:exectime => 0.0, :total => 0.0, :name => "webapp2 w/Jinja"},
  'web2simpletemplate' => {:exectime => 0.0, :total => 0.0, :name => "webapp2 w/SimpleTemplate"},
  'web2tenjin' => {:exectime => 0.0, :total => 0.0, :name => "webapp2 w/Tenjin"},
  'web2templator' => {:exectime => 0.0, :total => 0.0, :name => "webapp2 w/Templator"},
  'webpytemplator' => {:exectime => 0.0, :total => 0.0, :name => "web.py w/Templator"},
  'webpybreve' => {:exectime => 0.0, :total => 0.0, :name => "web.py w/Breve"},
  'webpydjango' => {:exectime => 0.0, :total => 0.0, :name => "web.py w/Django"},
  'webpyjinja' => {:exectime => 0.0, :total => 0.0, :name => "web.py w/Jinja"},
  'webpymako' => {:exectime => 0.0, :total => 0.0, :name => "web.py w/Mako"},
  'webpysimpletemplate' => {:exectime => 0.0, :total => 0.0, :name => "web.py w/SimpleTemplate"},
  'webpytenjin' => {:exectime => 0.0, :total => 0.0, :name => "web.py w/Tenjin"},
  'flaskjinja' => {:exectime => 0.0, :total => 0.0, :name => "flask w/Jinja"},
  'flaskbreve' => {:exectime => 0.0, :total => 0.0, :name => "flask w/Breve"},
  'flaskdjango' => {:exectime => 0.0, :total => 0.0, :name => "flask w/Django"},
  'flaskmako' => {:exectime => 0.0, :total => 0.0, :name => "flask w/Mako"},
  'flasksimpletemplate' => {:exectime => 0.0, :total => 0.0, :name => "flask w/SimpleTemplate"},
  'flasktenjin' => {:exectime => 0.0, :total => 0.0, :name => "flask w/Tenjin"},
  'flasktemplator' => {:exectime => 0.0, :total => 0.0, :name => "flask w/Templator"},
  'tipfyjinja' => {:exectime => 0.0, :total => 0.0, :name => "tipfy w/Jinja"},
  'tipfybreve' => {:exectime => 0.0, :total => 0.0, :name => "tipfy w/Breve"},
  'tipfydjango' => {:exectime => 0.0, :total => 0.0, :name => "tipfy w/Django"},
  'tipfymako' => {:exectime => 0.0, :total => 0.0, :name => "tipfy w/Mako"},
  'tipfysimpletemplate' => {:exectime => 0.0, :total => 0.0, :name => "tipfy w/SimpleTemplate"},
  'tipfytenjin' => {:exectime => 0.0, :total => 0.0, :name => "tipfy w/Tenjin"},
  'tipfytemplator' => {:exectime => 0.0, :total => 0.0, :name => "tipfy w/Templator"},
  'webobjinja' => {:exectime => 0.0, :total => 0.0, :name => "webop w/Jinja"},
  'webobbreve' => {:exectime => 0.0, :total => 0.0, :name => "webop w/Breve"},
  'webobdjango' => {:exectime => 0.0, :total => 0.0, :name => "webop w/Django"},
  'webobmako' => {:exectime => 0.0, :total => 0.0, :name => "webop w/Mako"},
  'webobsimpletemplate' => {:exectime => 0.0, :total => 0.0, :name => "webop w/SimpleTemplate"},
  'webobtenjin' => {:exectime => 0.0, :total => 0.0, :name => "webop w/Tenjin"},
  'webobtemplator' => {:exectime => 0.0, :total => 0.0, :name => "webop w/Templator"},
  'wsgijinja' => {:exectime => 0.0, :total => 0.0, :name => "WSGI w/Jinja"},
  'wsgibreve' => {:exectime => 0.0, :total => 0.0, :name => "WSGI w/Breve"},
  'wsgidjango' => {:exectime => 0.0, :total => 0.0, :name => "WSGI w/Django"},
  'wsgimako' => {:exectime => 0.0, :total => 0.0, :name => "WSGI w/Mako"},
  'wsgisimpletemplate' => {:exectime => 0.0, :total => 0.0, :name => "WSGI w/SimpleTemplate"},
  'wsgitenjin' => {:exectime => 0.0, :total => 0.0, :name => "WSGI w/Tenjin"},
  'wsgitemplator' => {:exectime => 0.0, :total => 0.0, :name => "WSGI w/Templator"},
  'wbbtenjcache' => {:exectime => 0.0, :total => 0.0, :name => "webop w/TenjinCache"}
}

[10,100,1000].each do |rows|
  runTest(25,rows)
end

puts "Totals:"
$results.each_value.sort_by { |v| v[:total] }.each do |v|
  printf("%25s: | %7.3f seconds overall | score: %7.3f |\n",v[:name],v[:exectime],v[:total])
end
puts

puts "Templating Engines:"
engines = {"Mako" => 0.0, "Jinja" => 0.0, "Django" => 0.0, "Templator" => 0.0, "Tenjin" => 0.0, "Breve" => 0.0, "SimpleTemplate" => 0.0}
$results.each do |k,v|
  engines.each do |ek,ev|
    if k.include? ek.downcase
      engines[ek] += v[:exectime]
    end
  end
end

best = 1
engines.each_value.sort.each_with_index do |v,i|
  k = engines.index(v)
  rank = 0
  if i == 0
    rank = 1
    best = v
  else
    rank = v / best
  end
  printf("%15s: | %7.3fs overall | score: %7.3f |\n", k, v, rank)
end
puts

puts "Web Application Frameworks:"
frames = {"Bottle" => 0.0, "Flask" => 0.0, "webapp" => 0.0, "web2" => 0.0, "webpy" => 0.0, "tipfy" => 0.0, "webob" => 0.0, "WSGI" => 0.0}
$results.each do |k,v|
  frames.each do |ek,ev|
    if k.include? ek.downcase
      frames[ek] += v[:exectime]
    end
  end
end

best = 1
frames.each_value.sort.each_with_index do |v,i|
  k = frames.index(v)
  rank = 0
  if i == 0
    rank = 1
    best = v
  else
    rank = v / best
  end
  k = "wep.py" if k == "webpy"
  printf("%15s: | %7.3fs overall | score: %7.3f |\n", k, v, rank)
end
puts

best = 1
puts "Default Configurations:"
[
  $results['bottlesimpletemplate'],
  $results['webappdjango'],
  $results['webpytemplator'],
  $results['flaskjinja'],
  $results['tipfyjinja']
].sort_by { |v| v[:exectime] }.each_with_index do |v,i|
  rank = 0
  if i == 0
    rank = 1
    best = v[:exectime]
  else
    rank = v[:exectime] / best
  end
  printf("%25s: | %7.3fs overall | score: %7.3f |\n", v[:name], v[:exectime], rank)
end
puts


